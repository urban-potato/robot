import json
from typing import Any
import urllib.request

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
                "get_current_time",
            ],
        },
        "arguments": {
            "type": "object",
            "additionalProperties": True,
        },
    },
    "required": ["tool", "arguments"],
    "additionalProperties": False,
}


class SemanticToolRouter:
    def __init__(self, ollama_url: str, model: str):
        self.ollama_url = ollama_url
        self.model = model

    def route(self, message: str) -> ToolRoute:
        system_prompt = """
You are a semantic tool router.

Your only task is to determine whether the user's request requires
a tool and, if so, select the appropriate tool and its arguments.

Do not answer the user's request.
Do not explain your decision.
Return only the required structured result.

Available tools:

1. web_search

Use this tool when the request requires information from the internet,
including current, latest, recent, changing, or online information.

Also use it when the user explicitly asks to search, find, look up,
check, verify, or browse the internet.

Arguments:
{
    "query": "a concise search query matching the user's request"
}


2. web_page_read

Use this tool when the user asks about the contents of a specific
web page or provides a URL whose contents need to be inspected.

Arguments:
{
    "url": "the exact URL provided by the user"
}


3. get_current_time

Use this tool when the current date or time is required.

Arguments:
{}


4. No tool

Set "tool" to null when the request can be answered without external,
current, or online information.

Examples:

"What is recursion?"
→ {"tool": null, "arguments": {}}

"How does a pointer work in C++?"
→ {"tool": null, "arguments": {}}

"What is the latest version of Python?"
→ {"tool": "web_search", "arguments": {"query": "latest version of Python"}}

"What is the current version of Flutter?"
→ {"tool": "web_search", "arguments": {"query": "current version of Flutter"}}

"Find the official Python documentation."
→ {"tool": "web_search", "arguments": {"query": "official Python documentation"}}

"What does this page say? https://example.com"
→ {"tool": "web_page_read", "arguments": {"url": "https://example.com"}}

"What time is it?"
→ {"tool": "get_current_time", "arguments": {}}

Important:

Determine the meaning of the request, not merely individual keywords.

Do not use a tool merely because a technical term, product name,
or programming language appears in the request.

Stable explanations normally do not require a tool.

Current or changing information normally requires web_search.

A specific URL whose contents must be inspected requires
web_page_read.

A request requiring the current date or time requires
get_current_time.

Choose exactly one tool or null.

Do not invent URLs.

For web_search, generate a concise query that represents the
user's actual information need.

Return only the structured result.
"""

        request_data: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": system_prompt,
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
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request) as response:
            data = json.load(response)

        print(
            "Semantic router timing:",
            {
                key: round(data.get(key, 0) / 1_000_000_000, 3)
                for key in (
                    "total_duration",
                    "load_duration",
                    "prompt_eval_duration",
                    "eval_duration",
                )
            },
        )

        result = json.loads(data["message"]["content"])

        return ToolRoute(
            tool=result["tool"],
            arguments=result["arguments"],
        )
    