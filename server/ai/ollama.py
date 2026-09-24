import json
import urllib.request

from .provider import AIProvider
from tools.executor import execute_tool
from tools.registry import TIME_TOOL 


class OllamaProvider(AIProvider):
    def __init__(self, ollama_url: str, model: str):
        self.ollama_url = ollama_url
        self.model = model

    def _request(self, messages: list[dict]) -> dict:
        # request_data = {
        #     "model": self.model,
        #     "messages": messages,
        #     "tools": [TIME_TOOL],
        #     "think": False,
        #     "stream": False,
        # }

        request_data = {
            "model": self.model,
            "messages": messages,
            "tools": [TIME_TOOL],
            "think": False,
            "stream": False,
            "options": {
                "temperature": 0.2,
            },
        }

        request_body = json.dumps(request_data).encode("utf-8")

        request = urllib.request.Request(
            self.ollama_url,
            data=request_body,
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request) as response:
            return json.load(response)

    def chat(self, messages: list[dict]) -> str:
        response_data = self._request(messages)
        message = response_data["message"]

        if "tool_calls" not in message:
            return message["content"]

       
        tool_call = message["tool_calls"][0]

        tool_name = tool_call["function"]["name"]
        tool_arguments = tool_call["function"]["arguments"]

        tool_result = execute_tool(
            tool_name,
            tool_arguments,
        )

        messages.append(message)

        messages.append({
            "role": "tool",
            "tool_name": tool_name,
            "content": tool_result,
        })

        response_data = self._request(messages)

        return response_data["message"]["content"]

