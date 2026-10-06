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
time information:

- current time;
- today's date;
- current day;
- current weekday;
- current month;
- current year;
- current date and time;
- whether today is a weekend or weekday;
- date/time in a specific location.

Do NOT use this tool for weather, prices, exchange rates,
versions, releases, news, availability, or other current
information that is not date/time information.

Arguments:
- city: only a city explicitly mentioned by the user;
- country_code: only a country explicitly mentioned by the user,
  converted to ISO 3166-1 alpha-2;
- timezone: only a timezone explicitly mentioned by the user.

Never infer missing location information.

Never use the configured city, configured country code, or
configured timezone as tool arguments.

If the user does not explicitly mention a location, call this
tool with NO location arguments.

The tool uses the configured user timezone internally when no
location arguments are provided.

If the user explicitly mentions a city and country, pass both.
If only a city is mentioned, pass only city.
If only a country is mentioned, pass only country_code.
If a timezone is explicitly mentioned, pass timezone.

Only use location information that appears in the user's message.
""",
    parameters={
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": (
                    "A city explicitly mentioned by the user. "
                    "Use the standard English city name when obvious."
                ),
            },
            "country_code": {
                "type": "string",
                "description": (
                    "The ISO 3166-1 alpha-2 code of a country explicitly "
                    "mentioned by the user."
                ),
            },
            "timezone": {
                "type": "string",
                "description": (
                    "A standard IANA timezone explicitly mentioned by "
                    "the user."
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

An explicit request to search, find, look up, check, verify, or
find out requires web_search even when the subject itself is stable.

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

Return a concise query that directly represents the user's request.

Preserve the user's intended subject and scope.
Do not replace, reinterpret, narrow, or broaden it.

For example, if the user asks about weather, keep the query
about weather. Do not change it to rain or temperature unless
the user asks specifically about rain or temperature.

--------------------------------------------------
LOCATION
--------------------------------------------------

Some searches are location-dependent, for example:
- weather;
- local conditions;
- local availability;
- local events;
- local services.

For a location-dependent search:

1. If the user explicitly provides a location, use that location.
2. Otherwise, use the configured city from User Context.

The explicit user location ALWAYS has priority.

The selected location MUST appear in the final query.

For non-location-dependent searches, do not add the configured
city.

The configured city is a fallback ONLY for location-dependent
web searches. It is not a general default.

Do not use configured city information when the user explicitly
provided another location.

--------------------------------------------------
QUERY FIDELITY
--------------------------------------------------

Keep the query faithful to the user's request.

Preserve:
- the main subject;
- explicit names;
- explicit locations;
- relevant time information.

Do not infer a more specific request.

For example:

User asks about weather
-> query about weather

User asks about rain
-> query about rain

User asks about temperature
-> query about temperature

User asks about pointers in C++
-> query about pointers in C++

Do not substitute one subject for another.

Do not unnecessarily translate or transliterate explicit names.
""",
    parameters={
        "type": "object",
        "properties": {
            "query": {
                "type": "string",
                "description": (
                    "A concise search query faithful to the user's "
                    "request. For location-dependent searches, include "
                    "the explicit user location, or the configured city "
                    "when no location was explicitly provided."
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
