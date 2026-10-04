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
- the current month;
- the current year;
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
- other current information that is not date/time information.

Location parameters:
- If a city is explicitly provided, pass it as city.
- If a country is explicitly provided, pass its ISO 3166-1 alpha-2
  country code as country_code.
- If a timezone is explicitly provided, pass it as timezone.
- Do not invent missing location information.
- Do not pass the configured user location when the person did not
  explicitly provide a location.

If no location is provided, call the tool without location arguments.
The tool uses the configured user timezone in that case.""",
    parameters={
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": (
                    "The city explicitly mentioned by the person. Normalize "
                    "obvious translations or transliterations to the standard "
                    "English city name when reliable."
                ),
            },
            "country_code": {
                "type": "string",
                "description": (
                    "The ISO 3166-1 alpha-2 country code for a country "
                    "explicitly mentioned by the person. Convert the country "
                    "name to its ISO 3166-1 alpha-2 code."
                ),
            },
            "timezone": {
                "type": "string",
                "description": (
                    "The standard IANA timezone corresponding to a timezone "
                    "explicitly mentioned by the person. Normalize recognizable "
                    "non-standard timezone forms to the standard IANA timezone "
                    "name."
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
