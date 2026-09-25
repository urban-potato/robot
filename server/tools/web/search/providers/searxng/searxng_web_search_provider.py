import json
import urllib.parse
import urllib.request

from ...web_search_provider import WebSearchProvider
from ...types import SearchResult


class SearXNGWebSearchProvider(WebSearchProvider):
    def __init__(self, url: str):
        self.url = url

    def search(
        self,
        query: str,
    ) -> list[SearchResult]:
        params = urllib.parse.urlencode(
            {
                "q": query,
                "format": "json",
            }
        )

        request = urllib.request.Request(
            f"{self.url}/search?{params}",
        )

        with urllib.request.urlopen(request) as response:
            data = json.load(response)

        return [
            SearchResult(
                title=result["title"],
                url=result["url"],
                snippet=result["content"],
            )
            for result in data["results"]
        ]
    