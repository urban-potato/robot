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
USER INFO
==================================================

The user's city: {config.city}
The user's country code: {config.country_code}
The user's timezone: {config.timezone}

These values are configuration, NOT user input.

They have different roles:

GET_DATETIME:
- the user's city, country code and timezone from USER INFO are NOT used as an argument;
- only explicit location from the user's message may become
  a tool argument;
- with no explicit location, get_datetime receives no location
  arguments and uses the user's timezone internally.

WEB_SEARCH:
- the user's city from USER INFO is used only as the fallback location for
  location-dependent searches like weather, temperature, 
  traffic, establishment opening hours, local events etc;
- if the user explicitly provides a location, use that location
  instead;
- the selected location must appear in the search query;
- do not add the user's city to unrelated searches.

The user's city, country code and timezone from USER INFO is NOT a general default for all tools.
"""
    
    return "\n\n".join(
        [
            ROUTER_PROMPT,
            user_context,
        ]
    )
