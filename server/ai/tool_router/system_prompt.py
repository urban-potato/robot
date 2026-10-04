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

Use User Context only for location-specific WEB SEARCH.

For WEB SEARCH:
- if the user mentions a location, use that location;
- otherwise use the configured city from User Context.

For GET DATETIME:
- use only location information mentioned by the user;
- if the user mentions no location, return arguments: {{}};
- never copy the configured location into get_datetime arguments.

A location mentioned by the user always has priority over User Context.
"""

    return "\n\n".join(
        [
            user_context,
            ROUTER_PROMPT,
        ]
    )
