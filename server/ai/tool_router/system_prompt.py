from assistant.assistant_config import ASSISTANT_CONFIG
from .router_prompt import ROUTER_PROMPT



def build_system_prompt() -> str:
    user_context = f"""
## User Context
The person's city is {ASSISTANT_CONFIG.user.city}.
The person's country code is {ASSISTANT_CONFIG.user.country_code}.
The person's timezone is {ASSISTANT_CONFIG.user.timezone}.
"""

    return "\n\n".join([
        ROUTER_PROMPT,
        user_context,
    ])