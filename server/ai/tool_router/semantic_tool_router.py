import json
from typing import Any
import urllib.request

from .system_prompt import build_system_prompt

from .types import ToolRoute


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
    def __init__(self, ollama_url: str, model: str):
        self.ollama_url = ollama_url
        self.model = model
        self.system_prompt = build_system_prompt()

    def route(self, message: str) -> ToolRoute:
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
            data = json.load(response)

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

        result = json.loads(
            data["message"]["content"]
        )

        return ToolRoute(
            tool=result["tool"],
            arguments=result["arguments"],
            needs_clarification=result["needs_clarification"],
            clarification_question=result["clarification_question"],
        )
    