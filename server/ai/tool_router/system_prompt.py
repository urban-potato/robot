from assistant.assistant_config import ASSISTANT_CONFIG

from .router_prompt import ROUTER_PROMPT


def build_system_prompt() -> str:
    user_context = f"""
## User Context

Configured city: {ASSISTANT_CONFIG.user.city}
Configured country code: {ASSISTANT_CONFIG.user.country_code}
Configured timezone: {ASSISTANT_CONFIG.user.timezone}

These values are authoritative.

For a datetime request without an explicit city:
- use the configured city;
- use the configured country code.

For a location-specific web search without an explicit city:
- include the configured city in the search query.

The explicitly requested city always has priority over the configured city.

Use the standard city name when a city is needed by get_datetime.
"""

    return "\n\n".join([
        ROUTER_PROMPT,
        user_context,
    ])
