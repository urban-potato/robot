from dataclasses import dataclass
from typing import Any, Callable

from .datetime.time_tools import get_current_time
from .factory import create_web_page_tool, create_web_search_tool


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict[str, Any]
    function: Callable[..., str]


TIME_TOOL = Tool(
    name="get_current_time",
    description="Get the current date and time.",
    parameters={
        "type": "object",
        "properties": {},
        "required": [],
    },
    function=get_current_time,
)

web_search_tool = create_web_search_tool()

WEB_SEARCH_TOOL = Tool(
    name="web_search",
    description="Search the web for information.",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "The search query.",
            },
        },
        "required": ["query"],
    },
    function=web_search_tool.search,
)

web_page_tool = create_web_page_tool()

WEB_PAGE_TOOL = Tool(
    name="web_page_read",
    description="Read the content of a web page.",
    parameters={
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The URL of the web page to read.",
            },
        },
        "required": ["url"],
    },
    function=web_page_tool.read,
)


TOOLS = {
    TIME_TOOL.name: TIME_TOOL,
    WEB_SEARCH_TOOL.name: WEB_SEARCH_TOOL,
    WEB_PAGE_TOOL.name: WEB_PAGE_TOOL,
}