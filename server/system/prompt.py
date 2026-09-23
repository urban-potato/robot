from .robot_config import ROBOT_CONFIG


CAPABILITIES_PROMPT = """
Your current main capabilities are communicating with the person and helping with various tasks
based on the knowledge available to you.

In the future, you will gain additional capabilities:
searching for information on the internet, controlling the computer,
a physical body with motors and servos, a camera,
and various sensors.

Do not claim that you already have a capability that we have not yet connected.
If a capability is planned for the future, treat it as a future capability,
not as one that is currently available.
"""


def build_system_prompt() -> str:
    identity = ROBOT_CONFIG.identity.format(
        ROBOT_NAME=ROBOT_CONFIG.robot_name,
        USER_NAME=ROBOT_CONFIG.user_name,
    )

    user_info = (
        f"The person you are interacting with is named {ROBOT_CONFIG.user_name}.\n"
        f"The person's gender is {ROBOT_CONFIG.user_gender}."
    )

    return "\n\n".join([
        identity,
        user_info,
        CAPABILITIES_PROMPT,
    ])