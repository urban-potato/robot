from dataclasses import dataclass
from typing import Any, Callable

from .datetime.time_tools import get_current_time
from .factory import create_web_search_tool


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


TOOLS = {
    TIME_TOOL.name: TIME_TOOL,
    WEB_SEARCH_TOOL.name: WEB_SEARCH_TOOL,
}