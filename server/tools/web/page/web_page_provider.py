from abc import ABC, abstractmethod

from .types import PageContent


class WebPageProvider(ABC):
    @abstractmethod
    def fetch(
        self,
        url: str,
    ) -> PageContent:
        pass