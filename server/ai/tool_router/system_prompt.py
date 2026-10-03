from assistant.assistant_config import ASSISTANT_CONFIG
from assistant.types import UserConfig

from .router_prompt import ROUTER_PROMPT


def build_system_prompt(
        user_config: UserConfig | None = None,
) -> str:
    user_config = (
        user_config
        if user_config is not None
        else ASSISTANT_CONFIG.user
    )

    user_context = f"""
## User Context

Configured city: {user_config.city}
Configured country code: {user_config.country_code}
Configured timezone: {user_config.timezone}

These values are authoritative.

For a location-specific web search without an explicit city:
- include the configured city in the search query.

The explicitly requested city, country and timezone always have priority over 
the configured city, country code and timezone.
"""

    return "\n\n".join([
        ROUTER_PROMPT,
        user_context,
    ])
