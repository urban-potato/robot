from assistant.assistant_config import ASSISTANT_CONFIG
from assistant.types import UserConfig

from .router_prompt import ROUTER_PROMPT


def build_system_prompt(
    user_config: UserConfig | None = None,
) -> str:
    config = (
        user_config
        if user_config is not None
        else ASSISTANT_CONFIG.user
    )

    user_context = f"""
==================================================
USER CONTEXT
==================================================

Configured city: {config.city}
Configured country code: {config.country_code}
Configured timezone: {config.timezone}
"""
    main_rools = """

User Context provides default location information only.

It MUST NOT determine which tool to use.

For WEB SEARCH:

- if the user explicitly mentions a location, use that location;
- otherwise, if the request requires a location, use the configured city;
- the user's explicit location always has priority;
- include the location in the web_search query;
- do not add a location to searches that do not require one.

For GET DATETIME:

- use only location information explicitly mentioned by the user;
- if the user mentions no location, return arguments: {};
- never copy the configured city into get_datetime;
- never copy the configured country code into get_datetime;
- never copy the configured timezone into get_datetime.

Examples:

"What is Python?"
{
    "tool": "default_assistant",
}

"What is the latest Python version?"
{
    "tool": "web_search",
    "arguments": {
        "query": "..."
    },
}
query does not need the configured city

"What's the weather?"
{
    "tool": "web_search",
    "arguments": {
        "query": "..."
    },
}
query uses the configured city

"What time is it?"
{
    "tool": "get_datetime",
}

"Сколько времени в Токио?"
{
    "tool": "get_datetime"
    "arguments": {
        "city": "Tokyo",
    },
}

"What time is it in London, UK?"
{
    "tool": "get_datetime"
    "arguments": {
        "city": "London",
        "country_code": "GB"
    },
}
"""



    return "\n\n".join(
        [
            ROUTER_PROMPT,
            user_context,
            main_rools,
        ]
    )
