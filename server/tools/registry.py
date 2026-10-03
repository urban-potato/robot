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


DATETIME_TOOL = Tool(
    name="get_datetime",
    description="""Get the current date and time.

Use this tool ONLY when the person asks for:
- the current time;
- today's date;
- the current day of the week;
- the current date and time;
- the current date or time in a specific location.

Do NOT use this tool for:
- weather;
- prices;
- exchange rates;
- current versions;
- current releases;
- current events;
- news;
- availability;
- other information merely because it contains words such as
  "current", "now", "today", or "tomorrow".

Location parameters:
- Pass all location information explicitly provided by the person.
- If a city is provided, pass it as `city`.
- If a country is provided, convert it to its ISO 3166-1 alpha-2
  country code and pass it as `country_code`.
- If a timezone is provided, pass it as `timezone`.
- Do not omit a provided location parameter because another location
  parameter is also present.
- Do not invent location parameters that were not provided by the person.

Examples:
- "What time is it in London?" -> city="London"
- "What time is it in London UK?" -> city="London", country_code="GB"
- "What time is it in Japan?" -> country_code="JP"
- "What time is it in Europe London?" -> timezone="Europe/London"
- "What time is it?" -> no location parameters""",
    parameters={
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": (
                    "The city whose current date and time is requested "
                    "when a city is explicitly provided."
                ),
            },
            "country_code": {
                "type": "string",
                "description": (
                    "The ISO 3166-1 alpha-2 country code of the country "
                    "when a country is explicitly provided."
                ),
            },
            "timezone": {
                "type": "string",
                "description": (
                    "The IANA timezone name when a timezone is explicitly "
                    "provided, for example 'Europe/London' or 'Asia/Tokyo'. "
                ),
            },
        },
        "required": [],
        "additionalProperties": False,
    },
    function=get_datetime_str,
)


web_search_tool = create_web_search_tool()

WEB_SEARCH_TOOL = Tool(
    name="web_search",
    description="""Search the internet for information that cannot be
answered reliably without current or online information.

Use this tool for:
- current or latest information;
- recent or changing information;
- current versions or releases;
- current prices or exchange rates;
- weather or current conditions;
- availability;
- information explicitly requested to be searched,
  checked, looked up, found, or verified online;
- recent news;
- information that must be obtained from an online source.

Do NOT use this tool for:
- casual conversation;
- personal questions;
- definitions;
- stable explanations;
- reasoning;
- programming help;
- programming concepts;
- stable general knowledge.

A technical topic does not by itself require web search.

Return a concise search query that directly matches
the person's request.""",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "A concise search query directly related to "
                    "the person's request."
                ),
            },
        },
        "required": ["query"],
        "additionalProperties": False,
    },
    function=web_search_tool.search,
)


web_page_tool = create_web_page_tool()

WEB_PAGE_TOOL = Tool(
    name="web_page_read",
    description="""Read and extract information from a specific web page.

Use this tool when:
- the person provides a URL and asks about its contents;
- a specific page must be inspected;
- the requested information is contained in that page.

Preserve the exact URL.

Do NOT use this tool for general web searches.""",
    parameters={
        "type": "object",
        "properties": {
            "url": {
                "type": "string",
                "description": "The exact URL of the web page to read.",
            },
        },
        "required": ["url"],
        "additionalProperties": False,
    },
    function=web_page_tool.read,
)


TOOLS = {
    DATETIME_TOOL.name: DATETIME_TOOL,
    WEB_SEARCH_TOOL.name: WEB_SEARCH_TOOL,
    WEB_PAGE_TOOL.name: WEB_PAGE_TOOL,
}
