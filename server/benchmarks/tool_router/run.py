import ast
import csv
import io
import os
import re
import time
from contextlib import redirect_stdout
from pathlib import Path
from statistics import mean, median

from dotenv import load_dotenv

from ai.tool_router.semantic_tool_router import SemanticToolRouter
from ai.tool_router.types import ToolRoute
from assistant.assistant_config import ASSISTANT_CONFIG

from .scenarios import TEST_GROUPS, ToolRouteTest
from .types import OllamaTiming, ResultRow


load_dotenv()


BENCHMARK_DIR = Path(__file__).resolve().parent
RESULTS_DIR = BENCHMARK_DIR / "results"
CSV_PATH = RESULTS_DIR / "results.csv"

OLLAMA_URL = os.environ["OLLAMA_URL"]
OLLAMA_MODEL = os.environ["OLLAMA_MODEL"]


router = SemanticToolRouter(
    ollama_url=OLLAMA_URL,
    model=OLLAMA_MODEL,
)


def parse_ollama_timing(
    output: str,
) -> OllamaTiming:
    match = re.search(
        r"Semantic router timing:\s*(\{.*?\})",
        output,
    )

    if not match:
        return {
            "ollama_total": None,
            "load": None,
            "prompt_eval": None,
            "eval": None,
        }

    timing = ast.literal_eval(match.group(1))

    return {
        "ollama_total": timing.get("total_duration"),
        "load": timing.get("load_duration"),
        "prompt_eval": timing.get("prompt_eval_duration"),
        "eval": timing.get("eval_duration"),
    }


def resolve_expected_query_parts(
    parts: tuple[str, ...],
) -> tuple[str, ...]:
    city = ASSISTANT_CONFIG.user.city
    country_code = ASSISTANT_CONFIG.user.country_code

    return tuple(
        part.replace(
            "__USER_CITY__",
            city,
        ).replace(
            "__USER_COUNTRY_CODE__",
            country_code,
        )
        for part in parts
    )


def validate_structure(
    result: ToolRoute,
) -> list[str]:
    errors: list[str] = []

    if result.needs_clarification:
        if result.tool is not None:
            errors.append(
                "clarification has a tool"
            )

        if result.arguments:
            errors.append(
                "clarification has arguments"
            )

        if not result.clarification_question:
            errors.append(
                "clarification_question is missing"
            )

    else:
        if result.clarification_question is not None:
            errors.append(
                "clarification_question must be None"
            )

    if result.tool is None and result.arguments:
        errors.append(
            "arguments must be empty when tool is None"
        )

    return errors


def validate_tool(
    test: ToolRouteTest,
    result: ToolRoute,
) -> list[str]:
    errors: list[str] = []

    if result.tool != test.expected_tool:
        errors.append(
            f"tool: expected {test.expected_tool!r}, "
            f"got {result.tool!r}"
        )

    if result.needs_clarification != test.expected_clarification:
        errors.append(
            "needs_clarification: "
            f"expected {test.expected_clarification!r}, "
            f"got {result.needs_clarification!r}"
        )

    if test.expected_tool == "web_search":
        query = result.arguments.get("query")

        if not isinstance(query, str):
            errors.append(
                "web_search query must be a string"
            )
            return errors

        if not query.strip():
            errors.append(
                "web_search query must not be empty"
            )
            return errors

        expected_query_parts = (
            resolve_expected_query_parts(
                test.expected_query_contains
            )
        )

        query_lower = query.casefold()

        for part in expected_query_parts:
            if part.casefold() not in query_lower:
                errors.append(
                    "web_search query does not contain "
                    f"expected value {part!r}: {query!r}"
                )

        return errors

    if result.arguments != test.expected_arguments:
        errors.append(
            "arguments: "
            f"expected {test.expected_arguments!r}, "
            f"got {result.arguments!r}"
        )

    return errors


def validate_result(
    test: ToolRouteTest,
    result: ToolRoute,
) -> list[str]:
    errors = validate_structure(result)
    errors.extend(
        validate_tool(
            test,
            result,
        )
    )

    return errors


def collect_timing_values(
    successful: list[ResultRow],
) -> list[tuple[str, list[float]]]:
    timing_values: list[tuple[str, list[float]]] = [
        (
            "Ollama total",
            [
                row["ollama_total"]
                for row in successful
                if row["ollama_total"] is not None
            ],
        ),
        (
            "Model load",
            [
                row["load"]
                for row in successful
                if row["load"] is not None
            ],
        ),
        (
            "Prompt evaluation",
            [
                row["prompt_eval"]
                for row in successful
                if row["prompt_eval"] is not None
            ],
        ),
        (
            "Token generation",
            [
                row["eval"]
                for row in successful
                if row["eval"] is not None
            ],
        ),
    ]

    return timing_values


def run_tests() -> None:
    tests = [
        (group_name, test)
        for group_name, group_tests in TEST_GROUPS
        for test in group_tests
    ]

    total_tests = len(tests)
    results: list[ResultRow] = []

    RESULTS_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    print(f"Model: {router.model}")
    print(f"Tests: {total_tests}")
    print("=" * 70)

    for index, (group, test) in enumerate(
        tests,
        start=1,
    ):
        captured = io.StringIO()

        start = time.perf_counter()

        try:
            with redirect_stdout(captured):
                result = router.route(test.message)

            elapsed = time.perf_counter() - start

            ollama = parse_ollama_timing(
                captured.getvalue()
            )

            errors = validate_result(
                test,
                result,
            )

            row: ResultRow = {
                "test": index,
                "group": group,
                "message": test.message,
                "wall_time": round(
                    elapsed,
                    3,
                ),
                "ollama_total": ollama["ollama_total"],
                "load": ollama["load"],
                "prompt_eval": ollama["prompt_eval"],
                "eval": ollama["eval"],
                "tool": result.tool,
                "arguments": result.arguments,
                "needs_clarification": (
                    result.needs_clarification
                ),
                "clarification_question": (
                    result.clarification_question
                ),
                "route_correct": not errors,
                "validation_errors": (
                    " | ".join(errors)
                ),
                "error": "",
            }

        except Exception as error:
            elapsed = time.perf_counter() - start

            ollama = parse_ollama_timing(
                captured.getvalue()
            )

            row = {
                "test": index,
                "group": group,
                "message": test.message,
                "wall_time": round(
                    elapsed,
                    3,
                ),
                "ollama_total": ollama["ollama_total"],
                "load": ollama["load"],
                "prompt_eval": ollama["prompt_eval"],
                "eval": ollama["eval"],
                "tool": None,
                "arguments": None,
                "needs_clarification": None,
                "clarification_question": None,
                "route_correct": False,
                "validation_errors": "",
                "error": (
                    f"{type(error).__name__}: {error}"
                ),
            }

        results.append(row)

        status = (
            "PASS"
            if row["route_correct"]
            and not row["error"]
            else "FAIL"
        )

        print(
            f"[{index:03}/{total_tests}] "
            f"{status} | "
            f"{elapsed:.3f} s | "
            f"Ollama: {row['ollama_total']} s | "
            f"Tool: {row['tool']} | "
            f"{test.message}"
        )

        if row["validation_errors"]:
            print(
                f"    {row['validation_errors']}"
            )

        if row["error"]:
            print(
                f"    {row['error']}"
            )

    fieldnames = [
        "test",
        "group",
        "message",
        "wall_time",
        "ollama_total",
        "load",
        "prompt_eval",
        "eval",
        "tool",
        "arguments",
        "needs_clarification",
        "clarification_question",
        "route_correct",
        "validation_errors",
        "error",
    ]

    with CSV_PATH.open(
        "w",
        encoding="utf-8-sig",
        newline="",
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
        )

        writer.writeheader()
        writer.writerows(results)

    successful = [
        row
        for row in results
        if not row["error"]
    ]

    correct = [
        row
        for row in results
        if row["route_correct"]
        and not row["error"]
    ]

    times: list[float] = [
        row["wall_time"]
        for row in successful
    ]

    print("\n" + "=" * 70)
    print("BENCHMARK SUMMARY")
    print("=" * 70)

    print(
        f"Correct routes:   "
        f"{len(correct)}/{total_tests}"
    )

    print(
        f"Successful tests: "
        f"{len(successful)}/{total_tests}"
    )

    print(
        f"Failed routes:    "
        f"{total_tests - len(correct)}"
    )

    if times:
        print(
            f"Total wall time:  "
            f"{sum(times):.3f} s"
        )

        print(
            f"Average:          "
            f"{mean(times):.3f} s"
        )

        print(
            f"Median:           "
            f"{median(times):.3f} s"
        )

        print(
            f"Minimum:          "
            f"{min(times):.3f} s"
        )

        print(
            f"Maximum:          "
            f"{max(times):.3f} s"
        )

        warm_times: list[float] = times[1:]

        if warm_times:
            print("\nWithout first request:")

            print(
                f"Average:          "
                f"{mean(warm_times):.3f} s"
            )

            print(
                f"Median:           "
                f"{median(warm_times):.3f} s"
            )

    print()

    timing_values = collect_timing_values(
        successful
    )

    for label, values in timing_values:
        if values:
            print(
                f"{label + ':':22}"
                f"{mean(values):.3f} s"
            )

    print(
        f"\nCSV saved to: {CSV_PATH}"
    )


if __name__ == "__main__":
    run_tests()
    