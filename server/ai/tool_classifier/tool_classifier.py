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

Your only task is to set "needs_web" to true or false.

IMPORTANT:
Missing web access when it is needed is a critical error.
Using the web when it is not strictly necessary is acceptable.

Therefore, prefer true whenever there is reasonable uncertainty.
Choose false only when you are confident that the request can be
answered without current or online information.

Set needs_web to true if ANY of these conditions apply:
- the user asks for current, latest, newest, recent, updated, or
  up-to-date information;
- the user asks what is currently supported, recommended, available,
  used, or considered standard;
- the user asks what changed in a recent or latest release, version,
  update, or event;
- the answer depends on information that may have changed over time;
- the user explicitly asks to search, find, look up, check, verify,
  browse, or search the internet;
- the user asks for information from a specific website, page,
  documentation, repository, or online source;
- the user asks for an official source, official documentation,
  official website, or online resource;
- the user asks about a current person holding a position or role;
- the user asks for current prices, weather, availability, schedules,
  news, releases, versions, or other changing information;
- the request contains a specific online source that must be inspected.

Set needs_web to false only when the request is stable knowledge,
general explanation, calculation, reasoning, or another task that
does not require current or online information.

IMPORTANT DISTINCTION:

"How does X work?" usually does not require the web.

"How is X currently recommended?" requires the web.

"What is X?" usually does not require the web.

"What is the latest/current version of X?" requires the web.

"What changed in X?" requires the web when X refers to a recent,
latest, or current version/release.

If the request could reasonably be interpreted as requiring
current information, choose true.

If the request could reasonably benefit from checking an online
source, choose true.

Do not rely on your own knowledge being sufficient.
The question is whether the information should be checked online.

Examples:

User request: "What is a robot?"
needs_web: false

User request: "How does recursion work?"
needs_web: false

User request: "What is the difference between a process and a thread?"
needs_web: false

User request: "What is TCP?"
needs_web: false

User request: "What is the latest version of Python?"
needs_web: true

User request: "What is the current version of Flutter?"
needs_web: true

User request: "Which Python version is currently supported?"
needs_web: true

User request: "What changed in the latest Python release?"
needs_web: true

User request: "How is Python threading currently recommended?"
needs_web: true

User request: "How is Python threading generally implemented?"
needs_web: false

User request: "How does Python store objects in memory?"
needs_web: false

User request: "What is currently recommended for Python concurrency?"
needs_web: true

User request: "Find the official Python website."
needs_web: true

User request: "Find the Ollama documentation for structured outputs."
needs_web: true

User request: "What does the Ollama documentation currently say about structured outputs?"
needs_web: true

User request: "Find the xiaozhi-esp32 repository on GitHub."
needs_web: true

User request: "What is ESP32?"
needs_web: false

User request: "What is ESP-IDF?"
needs_web: false

User request: "What is the latest ESP-IDF version?"
needs_web: true

User request: "How many bytes are in a kilobyte?"
needs_web: false

User request: "Who is currently the president of France?"
needs_web: true

User request: "What is a pointer in C++?"
needs_web: false

User request: "What changed in the latest C++ standard?"
needs_web: true

User request: "Explain how a call stack works."
needs_web: false

User request: "What is the weather tomorrow in London?"
needs_web: true

User request: "How much does the dollar cost right now?"
needs_web: true

User request: "Search the internet for information about ESP32-S3."
needs_web: true

Remember:

A false negative is worse than a false positive.

If you are unsure whether web access is required, set needs_web
to true.

Do not answer the user's request.
Do not explain your decision.
Return only the required structured result.
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
            "Classifier timing:",
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

        return ToolSelection(
            needs_web=result["needs_web"],
        )