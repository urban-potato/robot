from abc import ABC, abstractmethod

from conversation_memory.conversation_memory import ConversationMemory


class AIProvider(ABC):
    @abstractmethod
    def chat(
        self,
        memory: ConversationMemory,
    ) -> str:
        pass