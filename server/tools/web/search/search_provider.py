from abc import ABC, abstractmethod

from .types import SearchResult


class SearchProvider(ABC):
    @abstractmethod
    def search(
        self,
        query: str,
    ) -> list[SearchResult]:
        pass