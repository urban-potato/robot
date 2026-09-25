from .web_page_provider import WebPageProvider
from .types import PageContent


class WebPageTools:
    def __init__(
        self,
        provider: WebPageProvider,
    ):
        self.provider = provider

    def read(
        self,
        url: str,
    ) -> str:
        page = self.provider.fetch(url)

        return self._format_page(page)

    def _format_page(
        self,
        page: PageContent,
    ) -> str:
        return (
            f"Title: {page.title}\n"
            f"URL: {page.url}\n"
            f"Content:\n{page.text}"
        )