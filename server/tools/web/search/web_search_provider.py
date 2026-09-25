from abc import ABC, abstractmethod

from .types import SearchResult


class WebSearchProvider(ABC):
    @abstractmethod
    def search(
        self,
        query: str,
    ) -> list[SearchResult]:
        pass