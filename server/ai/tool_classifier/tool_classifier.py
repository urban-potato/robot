import json
from typing import Any
import urllib.request

from .types import ToolSelection


TOOL_SELECTION_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "needs_web": {
            "type": "boolean",
        },
    },
    "required": ["needs_web"],
    "additionalProperties": False,
}


class ToolClassifier:
    def __init__(self, ollama_url: str, model: str):
        self.ollama_url = ollama_url
        self.model = model

    def classify(self, message: str) -> ToolSelection:
        system_prompt = """
Determine whether the user's request requires using the web.

Set needs_web to true if the request asks for:
- current, latest, newest, recent, or up-to-date information;
- information that may have changed over time;
- information from a specific website or online source;
- information that the user explicitly asks you to search, find, or look up;
- an official website, page, documentation, or online resource.

Set needs_web to false if the request can be answered reliably
without accessing current online information.

When in doubt because the answer may have changed over time,
set needs_web to true.

Examples:

User request: "What is a robot?"
needs_web: false

User request: "How does recursion work?"
needs_web: false

User request: "What is the latest version of Python?"
needs_web: true

User request: "What is the current version of Flutter?"
needs_web: true

User request: "Find the official Python website."
needs_web: true

User request: "Find the Ollama documentation for structured outputs."
needs_web: true

User request: "Who is currently the president of France?"
needs_web: true

User request: "What is ESP32?"
needs_web: false

Do not answer the user's request.
Do not explain your decision.
"""

        request_data: dict[str, Any]  = {
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
            "format": TOOL_SELECTION_SCHEMA,
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

        result = json.loads(data["message"]["content"])

        return ToolSelection(
            needs_web=result["needs_web"],
        )