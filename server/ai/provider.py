from abc import ABC, abstractmethod
from typing import Any


class AIProvider(ABC):
    @abstractmethod
    def chat(self, messages: list[dict[str, Any]]) -> str:
        pass