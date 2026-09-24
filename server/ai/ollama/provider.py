from collections.abc import Sequence
import json
import urllib.request

from .types import OllamaOptions, OllamaRequest, OllamaRequestMessage, OllamaResponse, OllamaToolResultMessage
from ..provider import AIProvider
from memory import ConversationMemory, ConversationMemoryMessage, ConversationMemoryToolMessage
from tools.executor import ToolExecutionError, execute_tool
from tools.registry import TOOLS
from .mapper import get_ollama_tools


class OllamaProvider(AIProvider):
    def __init__(self, ollama_url: str, model: str):
        self.ollama_url = ollama_url
        self.model = model

    def _request(
        self,
        messages: Sequence[
            ConversationMemoryMessage | ConversationMemoryToolMessage
        ],
    ) -> OllamaResponse:
        request_messages = [
            (
                OllamaRequestMessage.from_memory_message(message)
                if isinstance(message, ConversationMemoryMessage)
                else OllamaToolResultMessage.from_memory_message(message)
            )
            for message in messages
        ]
        
        request_data = OllamaRequest(
            model=self.model,
            messages=request_messages,
            tools=get_ollama_tools(list(TOOLS.values())),
            think=False,
            stream=False,
            options=OllamaOptions(
                temperature=0.2,
            ),
        )

        request_body = json.dumps(
            request_data.to_dict()
        ).encode("utf-8")

        request = urllib.request.Request(
            self.ollama_url,
            data=request_body,
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request) as response:
            data = json.load(response)

        return OllamaResponse.from_dict(data)

    def chat(
        self,
        memory: ConversationMemory,
    ) -> str:
        while True:
            response_data = self._request(
                memory.get_messages()
            )

            message = response_data.message

            if not message.tool_calls:
                return message.content

            memory_message = message.to_memory_message()

            memory.add_assistant_message(
                memory_message.content,
                tool_calls=memory_message.tool_calls,
            )

            for tool_call in message.tool_calls:
                tool_name = tool_call.function.name

                try:
                    tool_result = execute_tool(
                        tool_name,
                        tool_call.function.arguments,
                    )
                except ToolExecutionError as error:
                    tool_result = str(error)

                memory.add_tool_message(
                    tool_name=tool_name,
                    content=tool_result,
                )
