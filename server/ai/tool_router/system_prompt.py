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

The following values are configured for the user:

Configured city: {config.city}
Configured country code: {config.country_code}
Configured timezone: {config.timezone}

IMPORTANT:

User Context is NOT part of the user's message.

It provides defaults only where explicitly allowed by the
router rules.

For GET_DATETIME:
- NEVER use these configured values unless the user explicitly
  mentions the corresponding location information.

For WEB_SEARCH:
- use the configured city only when the request is location-dependent
  and the user did not explicitly provide a location;
- include the configured city directly in the search query;
- do not add the configured city to unrelated searches.

Explicit user-provided location ALWAYS has priority over
configured location.
"""

    return "\n\n".join(
        [
            ROUTER_PROMPT,
            user_context,
        ]
    )
