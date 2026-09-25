from dataclasses import dataclass


@dataclass
class PageContent:
    url: str
    title: str
    text: str