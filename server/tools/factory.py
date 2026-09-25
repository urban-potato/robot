from config import SEARXNG_URL
from .web.search.providers.searxng.searxng_provider import SearXNGProvider
from .web.search.search_tools import WebSearchTool


def create_web_search_tool() -> WebSearchTool:
    provider = SearXNGProvider(
        url=SEARXNG_URL,
    )

    return WebSearchTool(
        provider=provider,
    )