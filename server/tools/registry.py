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

Use this tool when the requested information itself is date or
time information.

Use it for:
- current time;
- today's date;
- current day;
- current day of the week;
- current month;
- current year;
- current date and time;
- current date or time in a specific location;
- determining whether today is a weekend or weekday.

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
- If a city is explicitly mentioned, pass it as "city".
- If a country is explicitly mentioned, convert it to its
  ISO 3166-1 alpha-2 code and pass it as "country_code".
- If a timezone is explicitly mentioned, pass it as "timezone".
- Do not invent missing location information.
- Do not use configured user location unless the user explicitly
  mentioned that location.

If no location is explicitly provided, call the tool without
location arguments.

The tool uses the configured user timezone when no location
arguments are provided.""",
    parameters={
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": (
                    "A city explicitly mentioned by the person. "
                    "Normalize obvious translations or transliterations "
                    "to the standard English city name when reliable."
                ),
            },
            "country_code": {
                "type": "string",
                "description": (
                    "The ISO 3166-1 alpha-2 code of a country explicitly "
                    "mentioned by the person."
                ),
            },
            "timezone": {
                "type": "string",
                "description": (
                    "A standard IANA timezone explicitly mentioned by "
                    "the person. Normalize recognizable non-standard "
                    "timezone forms to the standard IANA name."
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
    description="""Search the internet.

Use this tool when the user explicitly asks to:
- search;
- find;
- look up;
- check;
- verify;
- find out;
- research;
- get information from online sources.

Also use this tool for information that is:
- current;
- latest;
- recent;
- changing;
- a current version;
- a latest release;
- a current price;
- an exchange rate;
- weather;
- current conditions;
- availability;
- recent news;
- other information that requires online information.

IMPORTANT:

An explicit request to search/find/look up/check/verify/find out
is enough to use this tool even when the subject itself is stable.

For example:
- "Search for information about Python."
- "Find information about TCP."
- "Look up recursion."
- "Find information about Flutter."

These MUST use web_search.

Do NOT use this tool for:
- stable definitions;
- stable explanations;
- conceptual questions;
- reasoning;
- ordinary programming help;
- programming concepts;
- debugging;
- casual conversation;
- personal questions;
- stable general knowledge.

A technical topic does not by itself require web search.

Return a concise search query that directly represents
the user's request.

For location-dependent searches:
- use an explicitly provided location when available;
- otherwise use the configured user city;
- include that location directly in the search query.""",
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
- the user provides a URL and asks about its contents;
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
