from dataclasses import dataclass, field
from typing import Any, TypedDict

from ai.tool_router.types import RouterTool


def _empty_arguments() -> dict[str, Any]:
    return {}


class OllamaTiming(TypedDict):
    ollama_total: float | None
    load: float | None
    prompt_eval: float | None
    eval: float | None


class ResultRow(TypedDict):
    test: int
    group: str
    message: str
    wall_time: float
    ollama_total: float | None
    load: float | None
    prompt_eval: float | None
    eval: float | None
    tool: str | None
    arguments: dict[str, Any] | None
    route_correct: bool
    validation_errors: str
    error: str


@dataclass(frozen=True)
class ToolRouteTest:
    message: str
    expected_tool: RouterTool

    # Arguments whose exact values must match.
    expected_arguments: dict[str, Any] = field(
        default_factory=_empty_arguments,
    )

    # Each tuple contains alternative words or phrases. The query must
    # contain at least one alternative from every tuple.
    expected_query_requirements: tuple[
        tuple[str, ...],
        ...,
    ] = ()
    