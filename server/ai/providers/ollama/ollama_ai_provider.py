from collections.abc import Sequence
import json
import urllib.request

from .types import OllamaOptions, OllamaRequest, OllamaRequestMessage, OllamaResponse, OllamaToolResultMessage
from ...ai_provider import AIProvider
from conversation_memory.conversation_memory import ConversationMemory
from conversation_memory.types import (
    ConversationMemoryMessage,
    ConversationMemoryToolMessage,
)
from tools.executor import ToolExecutionError, execute_tool
from tools.registry import TOOLS
from .ollama_mapper import get_ollama_tools


class OllamaAIProvider(AIProvider):
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

        # print('REQUEST:')
        # print(request_data.to_dict())
        # print(json.dumps(
        #     request_data.to_dict(),
        #     ensure_ascii=False,
        #     indent=2,
        # ))

        # request_body = json.dumps(
        #     request_data.to_dict()
        # ).encode("utf-8")

        request_body = json.dumps(
            request_data.to_dict(),
            ensure_ascii=False,
            indent=2,
        ).encode("utf-8")

        # TODO: temp print

        with open("ollama_request.tmp.json", "wb") as file:
            file.write(request_body)

        request = urllib.request.Request(
            self.ollama_url,
            data=request_body,
            headers={"Content-Type": "application/json"},
        )

        with urllib.request.urlopen(request) as response:
            data = json.load(response)
            print('RESPONSE:')
            print(data)

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
                # print(memory.messages)
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
                    tool_call_id=tool_call.id,
                    tool_name=tool_name,
                    content=tool_result,
                )
