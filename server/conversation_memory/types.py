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

