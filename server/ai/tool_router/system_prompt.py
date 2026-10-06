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

These values are configuration, NOT user input.

They have different roles:

GET_DATETIME:
- configured location is NOT used as an argument;
- only explicit location from the user's message may become
  a tool argument;
- with no explicit location, get_datetime receives no location
  arguments and uses the configured timezone internally.

WEB_SEARCH:
- configured city is used only as the fallback location for
  location-dependent searches;
- if the user explicitly provides a location, use that location
  instead;
- the selected location must appear in the search query;
- do not add the configured city to unrelated searches.

Configured location is NOT a general default for all tools.
"""
    
    return "\n\n".join(
        [
            ROUTER_PROMPT,
            user_context,
        ]
    )
