from abc import ABC, abstractmethod
from collections.abc import Sequence

from conversation_memory.conversation_memory import ConversationMemory
from tools.registry import Tool


class AIProvider(ABC):
    @abstractmethod
    def chat(
        self,
        memory: ConversationMemory,
        tools: Sequence[Tool] | None = None,
    ) -> str:
        pass