from dataclasses import dataclass


@dataclass
class ConversationMemoryToolCall:
    name: str
    arguments: dict[str, object]


@dataclass
class ConversationMemoryMessage:
    role: str
    content: str
    tool_calls: list[ConversationMemoryToolCall] | None = None


@dataclass
class ConversationMemoryToolMessage:
    tool_name: str
    content: str


class ConversationMemory:
    def __init__(self, system_prompt: str):
        self.messages: list[
            ConversationMemoryMessage | ConversationMemoryToolMessage
        ] = [
            ConversationMemoryMessage(
                role="system",
                content=system_prompt,
            )
        ]

    def add_user_message(self, message: str):
        self.messages.append(
            ConversationMemoryMessage(
                role="user",
                content=message,
            )
        )

    def add_assistant_message(
        self,
        message: str,
        tool_calls: list[ConversationMemoryToolCall] | None = None,
    ):
        self.messages.append(
            ConversationMemoryMessage(
                role="assistant",
                content=message,
                tool_calls=tool_calls,
            )
        )

    def add_tool_message(
        self,
        tool_name: str,
        content: str,
    ):
        self.messages.append(
            ConversationMemoryToolMessage(
                tool_name=tool_name,
                content=content,
            )
        )

    def get_messages(
        self,
    ) -> list[ConversationMemoryMessage | ConversationMemoryToolMessage]:
        return self.messages.copy()
    