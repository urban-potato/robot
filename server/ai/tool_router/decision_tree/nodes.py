import json
import re
import urllib.request
from typing import Any


URL_PATTERN = re.compile(
    r"https?://[^\s<>\"]+",
    re.IGNORECASE,
)


def extract_url(message: str) -> str | None:
    """
    Extract the first explicit HTTP/HTTPS URL from the message.

    This is deliberately deterministic.
    We don't need an LLM to answer the question:
    "Is there a URL in this text?"
    """

    match = URL_PATTERN.search(message)

    if match is None:
        return None

    return match.group(0).rstrip(".,!?;:)]}")


class DecisionTreeLLM:
    """
    Small helper responsible only for calling Ollama.

    The actual decision logic remains in DecisionTreeRouter.
    """

    def __init__(self, ollama_url: str, model: str):
        self.ollama_url = ollama_url
        self.model = model

    def classify_binary(
        self,
        system_prompt: str,
        message: str,
    ) -> bool:
        """
        Ask the model one binary yes/no question.

        Expected response:
            {"answer": true}

        or:
            {"answer": false}
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
            "format": {
                "type": "object",
                "properties": {
                    "answer": {
                        "type": "boolean",
                    },
                },
                "required": ["answer"],
                "additionalProperties": False,
            },
            "options": {
                "temperature": 0,
            },
        }

        return self.request(request_data)["answer"]

    def generate_search_query(
        self,
        system_prompt: str,
        message: str,
    ) -> str:
        """
        Generate a search query after the tree has already decided
        that web_search is required.
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
            "format": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                    },
                },
                "required": ["query"],
                "additionalProperties": False,
            },
            "options": {
                "temperature": 0,
            },
        }

        return self.request(request_data)["query"]

    def request(
        self,
        request_data: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Send one request to Ollama and parse the JSON response.
        """

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

        with urllib.request.urlopen(request) as response:
            data = json.load(response)

        return json.loads(
            data["message"]["content"]
        )
    