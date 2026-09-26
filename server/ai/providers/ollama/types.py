from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Sequence

from conversation_memory.conversation_memory import ConversationMemoryMessage, ConversationMemoryToolCall, ConversationMemoryToolMessage


@dataclass
class OllamaFunction:
    index: int
    name: str
    arguments: dict[str, object]


@dataclass
class OllamaToolCall:
    id: str
    function: OllamaFunction


@dataclass
class OllamaOptions:
    temperature: float


@dataclass
class OllamaRequestMessage:
    role: str
    content: str
    tool_calls: list[OllamaToolCall] | None = None

    @staticmethod
    def from_memory_message(
        message: ConversationMemoryMessage,
    ) -> OllamaRequestMessage:
        tool_calls = None

        if message.tool_calls is not None:
            tool_calls = [
                OllamaToolCall(
                    id=tool_call.id,
                    function=OllamaFunction(
                        index=tool_call.index,
                        name=tool_call.name,
                        arguments=tool_call.arguments,
                    ),
                )
                for tool_call in message.tool_calls
            ]

        return OllamaRequestMessage(
            role=message.role,
            content=message.content,
            tool_calls=tool_calls,
        )


    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> OllamaRequestMessage:
        tool_calls = None

        if "tool_calls" in data:
            tool_calls = [
                OllamaToolCall(
                    id=call["id"],
                    function=OllamaFunction(
                        index=call["function"]["index"],
                        name=call["function"]["name"],
                        arguments=call["function"]["arguments"],
                    ),
                )
                for call in data["tool_calls"]
            ]

        return cls(
            role=data["role"],
            content=data["content"],
            tool_calls=tool_calls,
        )

    def to_dict(self) -> dict[str, Any]:
        message: dict[str, Any] = {
            "role": self.role,
            "content": self.content,
        }

        if self.tool_calls is not None:
            message["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "function": {
                        "index": tool_call.function.index,
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    },
                }
                for tool_call in self.tool_calls
            ]

        return message


@dataclass
class OllamaToolResultMessage:
    content: str
    tool_name: str
    tool_call_id: str

    @classmethod
    def from_memory_message(
        cls,
        message: ConversationMemoryToolMessage,
    ) -> OllamaToolResultMessage:
        return cls(
            content=message.content,
            tool_name=message.tool_name,
            tool_call_id=message.tool_call_id,
            
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "role": "tool",
            "content": self.content,
            "tool_name": self.tool_name,
            # "tool_call_id": self.tool_call_id,
        }


@dataclass
class OllamaRequest:
    model: str
    messages: Sequence[OllamaRequestMessage | OllamaToolResultMessage]
    tools: list[dict[str, Any]]
    think: bool
    stream: bool
    options: OllamaOptions

    def to_dict(self) -> dict[str, Any]:
        return {
            "model": self.model,
            "messages": [
                message.to_dict()
                for message in self.messages
            ],
            "tools": self.tools,
            "think": self.think,
            "stream": self.stream,
            "options": {
                "temperature": self.options.temperature,
            },
        }


@dataclass
class OllamaResponseMessage:
    role: str
    content: str
    tool_calls: list[OllamaToolCall] | None = None

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> OllamaResponseMessage:
        tool_calls = None

        if "tool_calls" in data:
            tool_calls = [
                OllamaToolCall(
                    id=call["id"],
                    function=OllamaFunction(
                        index=call["function"]["index"],
                        name=call["function"]["name"],
                        arguments=call["function"]["arguments"],
                    ),
                )
                for call in data["tool_calls"]
            ]

        return cls(
            role=data["role"],
            content=data["content"],
            tool_calls=tool_calls,
        )

    def to_memory_message(self) -> ConversationMemoryMessage:
        tool_calls = None

        if self.tool_calls is not None:
            tool_calls = [
                ConversationMemoryToolCall(
                    id=tool_call.id,
                    index=tool_call.function.index,
                    name=tool_call.function.name,
                    arguments=tool_call.function.arguments,
                )
                for tool_call in self.tool_calls
            ]

        return ConversationMemoryMessage(
            role=self.role,
            content=self.content,
            tool_calls=tool_calls,
        )

    # def to_request_message(self) -> OllamaRequestMessage:
    #     return OllamaRequestMessage(
    #         role=self.role,
    #         content=self.content,
    #         tool_calls=self.tool_calls,
    #     )




@dataclass
class OllamaResponse:
    message: OllamaResponseMessage

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any],
    ) -> OllamaResponse:
        return cls(
            message=OllamaResponseMessage.from_dict(
                data["message"],
            ),
        )