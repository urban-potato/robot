from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from assistant.assistant_config import ASSISTANT_CONFIG
from .types import DateTimeResult
from .helpers.resolve_timezone import resolve_timezone


def get_datetime(
    city: str | None = None,
    country_code: str | None = None,
) -> DateTimeResult:
    if city is not None:
        timezone_name = resolve_timezone(city, country_code)
    else:
        timezone_name = ASSISTANT_CONFIG.user.timezone

        if not timezone_name:
            raise ValueError(
                "User timezone is not configured."
            )

    try:
        timezone = ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as error:
        raise ValueError(
            f"Invalid timezone: {timezone_name!r}."
        ) from error

    current_datetime = datetime.now(timezone)

    return {
        "datetime": current_datetime.isoformat(),
        "date": current_datetime.strftime("%Y-%m-%d"),
        "time": current_datetime.strftime("%H:%M:%S"),
        "weekday": current_datetime.isoweekday(),
        "day": current_datetime.day,
        "month": current_datetime.month,
        "year": current_datetime.year,
        "timezone": timezone_name,
        "utc_offset": current_datetime.strftime("%z"),
    }

def get_datetime_str(
    city: str | None = None,
    country_code: str | None = None,
) -> str:
    result = get_datetime(city, country_code)

    return "\n".join(
        f"{key}: {value}"
        for key, value in result.items()
    )