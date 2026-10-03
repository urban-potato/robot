import json
import urllib.request
from typing import Any, cast

from assistant.assistant_config import ASSISTANT_CONFIG
from assistant.types import UserConfig

from .system_prompt import build_system_prompt
from .types import ToolRoute


TOOL_NAMES: set[str | None] = {
    None,
    "web_search",
    "web_page_read",
    "get_datetime",
}


TOOL_ROUTE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "tool": {
            "type": ["string", "null"],
            "enum": [
                None,
                "web_search",
                "web_page_read",
                "get_datetime",
            ],
        },
        "arguments": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                },
                "url": {
                    "type": "string",
                },
                "city": {
                    "type": "string",
                },
                "country_code": {
                    "type": "string",
                },
            },
            "additionalProperties": False,
        },
        "needs_clarification": {
            "type": "boolean",
        },
        "clarification_question": {
            "type": ["string", "null"],
        },
    },
    "required": [
        "tool",
        "arguments",
        "needs_clarification",
        "clarification_question",
    ],
    "additionalProperties": False,
}


class SemanticToolRouter:
    def __init__(
        self,
        ollama_url: str,
        model: str,
        user_config: UserConfig | None = None,
    ):
        self.ollama_url = ollama_url
        self.model = model
        self.system_prompt = build_system_prompt(user_config)

    def route(
        self,
        message: str,
    ) -> ToolRoute:
        request_data: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": self.system_prompt,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
            "stream": False,
            "format": TOOL_ROUTE_SCHEMA,
            "options": {
                "temperature": 0,
            },
        }

        request_body = json.dumps(
            request_data,
            ensure_ascii=False,
        ).encode("utf-8")

        request = urllib.request.Request(
            self.ollama_url,
            data=request_body,
            headers={
                "Content-Type": "application/json",
            },
        )

        with urllib.request.urlopen(
            request,
            timeout=60,
        ) as response:
            data: Any = json.load(response)

        print(
            "Semantic router timing:",
            {
                key: round(
                    data.get(key, 0) / 1_000_000_000,
                    3,
                )
                for key in (
                    "total_duration",
                    "load_duration",
                    "prompt_eval_duration",
                    "eval_duration",
                )
            },
        )

        content = data["message"]["content"]

        if not isinstance(content, str):
            raise ValueError(
                "Ollama returned a non-string router response."
            )

        parsed: Any = json.loads(content)

        if not isinstance(parsed, dict):
            raise ValueError(
                "Router response must be a JSON object."
            )

        result = cast(
            dict[str, Any],
            parsed,
        )

        return self._build_route(result)

    def _build_route(
        self,
        result: dict[str, Any],
    ) -> ToolRoute:
        tool = result.get("tool")

        if tool is not None and not isinstance(tool, str):
            raise ValueError(
                "Router field 'tool' must be a string or null."
            )

        if tool not in TOOL_NAMES:
            raise ValueError(
                f"Unknown router tool: {tool!r}"
            )

        arguments = result.get("arguments", {})

        if not isinstance(arguments, dict):
            raise ValueError(
                "Router field 'arguments' must be an object."
            )

        arguments = cast(
            dict[str, Any],
            arguments,
        )

        needs_clarification = result.get(
            "needs_clarification"
        )

        if not isinstance(needs_clarification, bool):
            raise ValueError(
                "Router field 'needs_clarification' must be boolean."
            )

        clarification_question = result.get(
            "clarification_question"
        )

        if (
            clarification_question is not None
            and not isinstance(clarification_question, str)
        ):
            raise ValueError(
                "Router field 'clarification_question' must be a string "
                "or null."
            )

        normalized_arguments = self._normalize_arguments(
            tool,
            arguments,
        )

        if needs_clarification:
            return ToolRoute(
                tool=None,
                arguments={},
                needs_clarification=True,
                clarification_question=clarification_question,
            )

        return ToolRoute(
            tool=tool,
            arguments=normalized_arguments,
            needs_clarification=False,
            clarification_question=None,
        )

    def _normalize_arguments(
        self,
        tool: str | None,
        arguments: dict[str, Any],
    ) -> dict[str, str]:
        if tool is None:
            return {}

        if tool == "web_search":
            query = arguments.get("query")

            if not isinstance(query, str) or not query.strip():
                raise ValueError(
                    "web_search requires a non-empty string query."
                )

            return {
                "query": query.strip(),
            }

        if tool == "web_page_read":
            url = arguments.get("url")

            if not isinstance(url, str) or not url.strip():
                raise ValueError(
                    "web_page_read requires a non-empty string URL."
                )

            return {
                "url": url.strip(),
            }

        if tool == "get_datetime":
            city = arguments.get("city")
            country_code = arguments.get("country_code")

            if city is not None and not isinstance(city, str):
                raise ValueError(
                    "get_datetime city must be a string."
                )

            if (
                country_code is not None
                and not isinstance(country_code, str)
            ):
                raise ValueError(
                    "get_datetime country_code must be a string."
                )

            normalized_city = (
                city.strip()
                if isinstance(city, str)
                else ""
            )

            normalized_country_code = (
                country_code.strip().upper()
                if isinstance(country_code, str)
                else ""
            )

            if not normalized_city:
                normalized_city = ASSISTANT_CONFIG.user.city

            if not normalized_country_code:
                normalized_country_code = (
                    ASSISTANT_CONFIG.user.country_code
                )

            return {
                "city": normalized_city,
                "country_code": normalized_country_code,
            }

        raise ValueError(
            f"Unsupported router tool: {tool!r}"
        )
    