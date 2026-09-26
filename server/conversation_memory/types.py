from dataclasses import dataclass


@dataclass
class ConversationMemoryToolCall:
    id: str
    index: int
    name: str
    arguments: dict[str, object]


@dataclass
class ConversationMemoryMessage:
    role: str
    content: str
    tool_calls: list[ConversationMemoryToolCall] | None = None


@dataclass
class ConversationMemoryToolMessage:
    tool_call_id: str
    tool_name: str
    content: str



# @dataclass
# class ConversationMemoryToolCall:
#     id: str
#     name: str
#     arguments: dict[str, object]


# @dataclass
# class ConversationMemoryMessage:
#     role: str
#     content: str
#     tool_calls: list[ConversationMemoryToolCall] | None = None


# @dataclass
# class ConversationMemoryToolMessage:
#     tool_call_id: str
#     content: str

