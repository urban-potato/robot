
from .assistant_config import ASSISTANT_CONFIG

from .prompts.communication import COMMUNICATION_PROMPT
from .prompts.grounding import GROUNDING_PROMPT
from .prompts.tool_usage import TOOL_USAGE_PROMPT


def build_system_prompt() -> str:
    identity = ASSISTANT_CONFIG.identity.format(
        ROBOT_NAME=ASSISTANT_CONFIG.name,
        USER_NAME=ASSISTANT_CONFIG.user.name,
    )

    user_info = (
        f"The person I am interacting with is named "
        f"{ASSISTANT_CONFIG.user.name}.\n"
        f"I always write the person's name exactly as: "
        f"{ASSISTANT_CONFIG.user.name}.\n"
        f"I do not transliterate, translate, partially transliterate, "
        f"or mix alphabets in the person's name.\n"
        f"The person's gender is {ASSISTANT_CONFIG.user.gender}.\n"
        f"The person's timezone is {ASSISTANT_CONFIG.user.timezone}."
    )

    return "\n\n".join([
        identity,
        user_info,
        COMMUNICATION_PROMPT,
        GROUNDING_PROMPT,
        TOOL_USAGE_PROMPT,
    ])
