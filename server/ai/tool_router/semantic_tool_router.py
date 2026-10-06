import json
import urllib.request
from typing import Any, cast

from assistant.types import UserConfig
from .tool_route_schema import TOOL_ROUTE_SCHEMA
from .system_prompt import build_system_prompt
from .types import (
    RouterField,
    RouterTool,
    ToolRoute,
)


class SemanticToolRouter:
    def __init__(
        self,
        ollama_url: str,
        model: str,
        user_config: UserConfig | None = None,
    ):
        self.ollama_url = ollama_url
        self.model = model
        self.system_prompt = build_system_prompt(
            user_config,
        )

    def route(
        self,
        message: str,
    ) -> ToolRoute:
        response = self._chat(message)
        result = self._get_content(response)

        return self._build_route(result)

    def _get_content(
        self,
        response: Any,
    ) -> dict[str, Any]:
        content = response["message"]["content"]

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

        return result

    def _build_route(
        self,
        result: dict[str, Any],
    ) -> ToolRoute:
        tool_value = result.get(
            RouterField.TOOL,
        )

        if tool_value is not None and not isinstance(
            tool_value,
            str,
        ):
            raise ValueError(
                f"Router field {RouterField.TOOL!r} "
                "must be a string."
            )

        try:
            tool = RouterTool(tool_value)
        except ValueError as error:
            raise ValueError(
                f"Unknown router tool: {tool_value!r}"
            ) from error

        arguments = result.get(
            RouterField.ARGUMENTS,
            {},
        )

        if not isinstance(arguments, dict):
            raise ValueError(
                "Router field 'arguments' must be an object."
            )

        arguments = cast(
            dict[str, Any],
            arguments,
        )

        return ToolRoute(
            tool=tool,
            arguments=tool.normalize_arguments(
                arguments,
            ),
        )

    def _build_request_data(
        self,
        message: str,
    ) -> dict[str, Any]:
        return {
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
                # "num_ctx": 3072,
            },
        }

    def _print_info(
        self,
        data: Any,
    ) -> None:
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

    def _chat(
        self,
        message: str,
    ) -> Any:
        request_data = self._build_request_data(
            message,
        )

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

        self._print_info(data)

        return data
    