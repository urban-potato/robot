import json
import urllib.request

from .provider import AIProvider

class OllamaProvider(AIProvider):
    def __init__(self, ollama_url: str, model: str):
        self.ollama_url = ollama_url
        self.model = model

    def chat(self, message: str) -> str:
        request_data = {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": message,
                }
            ],
            "think": False,
            "stream": False,
        }

        request_body = json.dumps(request_data).encode("utf-8")

        request = urllib.request.Request(
            self.ollama_url,
            data=request_body,
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request) as response:
            response_data = json.load(response)

        return response_data["message"]["content"]