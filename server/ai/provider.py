from abc import ABC, abstractmethod

class AIProvider(ABC):
    @abstractmethod
    def chat(self, message: str) -> str:
        pass