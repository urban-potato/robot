from .search_provider import SearchProvider
from .types import SearchResult


class WebSearchTool:
    def __init__(
        self,
        provider: SearchProvider,
    ):
        self.provider = provider

    def search(
        self,
        query: str,
    ) -> str:
        results = self.provider.search(query)

        return self._format_results(results)

    def _format_results(
        self,
        results: list[SearchResult],
    ) -> str:
        return "\n\n".join(
            (
                f"Title: {result.title}\n"
                f"URL: {result.url}\n"
                f"Snippet: {result.snippet}"
            )
            for result in results
        )
    