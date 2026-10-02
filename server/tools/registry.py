from dataclasses import dataclass
from typing import Any, Callable

from .datetime.datetime_tools import get_datetime_str
from .factory import create_web_page_tool, create_web_search_tool


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict[str, Any]
    function: Callable[..., str]


TIME_TOOL = Tool(
    name="get_datetime",
    description="""Get the current date and time.

Use this tool when:
- the person asks for the current time or date;
- the person asks what day it is;
- the person asks for the current date or time in a specific city;
- the current date or time is needed to answer the request.

If a city is provided, use the city and country code extracted from
the person's request. If no city is provided, get the date and time
in the person's configured timezone.""",
    parameters={
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "The city whose current date and time is requested.",
            },
            "country_code": {
                "type": "string",
                "description": "The ISO 3166-1 alpha-2 country code of the city.",
            },
        },
        "required": [],
    },
    function=get_datetime_str,
)

web_search_tool = create_web_search_tool()

WEB_SEARCH_TOOL = Tool(
    name="web_search",
    description="""Search the internet for information that cannot be answered
reliably without up-to-date or online sources.

Use this tool for:
- current or latest information;
- recent or changing information;
- information the person explicitly asks you to search for;
- information that must be obtained from a website or online source.

Do not use this tool for casual conversation, personal questions,
definitions, explanations, or other requests that can be answered
without an online search.

Return a search query that directly matches the person's request.""",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": "A concise search query directly related to the person's request.",
            },
        },
        "required": ["query"],
    },
    function=web_search_tool.search,
)

web_page_tool = create_web_page_tool()

WEB_PAGE_TOOL = Tool(
    name="web_page_read",
    description="""Read and extract information from a specific web page.

Use this tool when:
- the person provides a URL and asks about its contents;
- a specific page found through web search must be inspected;
- the information needed is contained in the page itself and is not
available in the search result.

Do not use this tool for general web searches.""",
    parameters={
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The exact URL of the web page to read.",
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