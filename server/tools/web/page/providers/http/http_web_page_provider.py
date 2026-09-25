import gzip
import urllib.request

from bs4 import BeautifulSoup

from ...web_page_provider import WebPageProvider
from ...types import PageContent


class HttpWebPageProvider(WebPageProvider):
    def fetch(
        self,
        url: str,
    ) -> PageContent:
        request = urllib.request.Request(url)

        with urllib.request.urlopen(request) as response:
            html = response.read()

            if response.headers.get("Content-Encoding") == "gzip":
                html = gzip.decompress(html)

            html = html.decode("utf-8")

        soup = BeautifulSoup(html, "html.parser")

        title = soup.title.get_text(strip=True) if soup.title else ""

        text = soup.get_text(
            separator="\n",
            strip=True,
        )

        return PageContent(
            url=url,
            title=title,
            text=text,
        )
    