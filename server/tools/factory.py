from config import SEARXNG_URL

from .web.page.providers.http.http_web_page_provider import HttpWebPageProvider
from .web.page.web_page_tools import WebPageTools
from .web.search.providers.searxng.searxng_web_search_provider import SearXNGWebSearchProvider
from .web.search.web_search_tools import WebSearchTools


def create_web_search_tool() -> WebSearchTools:
    provider = SearXNGWebSearchProvider(
        url=SEARXNG_URL,
    )

    return WebSearchTools(
        provider=provider,
    )


def create_web_page_tool() -> WebPageTools:
    provider = HttpWebPageProvider()

    return WebPageTools(
        provider=provider,
    )