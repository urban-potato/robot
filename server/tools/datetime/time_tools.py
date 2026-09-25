from datetime import datetime
from zoneinfo import ZoneInfo

from assistant.assistant_config import ASSISTANT_CONFIG



def get_current_time() -> str:
    timezone = ZoneInfo(ASSISTANT_CONFIG.user.timezone)
    current_time = datetime.now(timezone)

    return (
        f"Current local time: {current_time:%Y-%m-%d %H:%M:%S}\n"
        f"Time zone: {ASSISTANT_CONFIG.user.timezone}\n"
        f"UTC offset: {current_time:%z}"
    )