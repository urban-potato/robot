from datetime import datetime
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from assistant.assistant_config import ASSISTANT_CONFIG

from .helpers.resolve_timezone import resolve_timezone
from .types import DateTimeResult


def get_datetime(
    city: str | None = None,
    country_code: str | None = None,
    timezone: str | None = None,
) -> DateTimeResult:
    """
    Returns the current date and time for the requested location.

    Timezone resolution uses the following priority:

    1. Explicit timezone.
       Example:
           get_datetime(timezone="Europe/London")
       Uses "Europe/London" directly.

    2. City with optional country code.
       Example:
           get_datetime(city="London")
       Searches for matching cities and selects the most likely one.

       Example:
           get_datetime(city="London", country_code="GB")
       Searches only for London in Great Britain.

       When the country code is omitted, matching cities are ranked by:
       - exact city name match;
       - population.

       Therefore:
           get_datetime(city="London")
       resolves to London, GB rather than treating the name as ambiguous.

    3. Country code without a city.
       Example:
           get_datetime(country_code="GB")
       Resolves the timezone from the country's available timezones.

       If the country has exactly one timezone, it is used.
       If the country has multiple timezones, a ValueError is raised
       because a more specific location is required.

    4. No location.
       Example:
           get_datetime()
       Uses the user's configured timezone from ASSISTANT_CONFIG.

    An explicit timezone always has priority over city and country_code.
    """
    
    timezone_name = _resolve_timezone(
        city=city,
        country_code=country_code,
        timezone=timezone,
    )

    try:
        timezone_info = ZoneInfo(timezone_name)
    except ZoneInfoNotFoundError as error:
        raise ValueError(
            f"Invalid timezone: {timezone_name!r}."
        ) from error

    current_datetime = datetime.now(timezone_info)

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
    timezone: str | None = None,
) -> str:
    result = get_datetime(
        city=city,
        country_code=country_code,
        timezone=timezone,
    )

    return "\n".join(
        f"{key}: {value}"
        for key, value in result.items()
    )


def _resolve_timezone(
    city: str | None,
    country_code: str | None,
    timezone: str | None,
) -> str:
    normalized_timezone = _normalize_timezone(timezone)

    if normalized_timezone is not None:
        return normalized_timezone

    normalized_city = _normalize_city(city)
    normalized_country_code = _normalize_country_code(country_code)

    if (
        normalized_city is not None
        or normalized_country_code is not None
    ):
        resolution = resolve_timezone(
            city=normalized_city,
            country_code=normalized_country_code,
        )

        return resolution["timezone"]

    user_timezone = ASSISTANT_CONFIG.user.timezone

    if not user_timezone:
        raise ValueError(
            "User timezone is not configured."
        )

    return user_timezone


def _normalize_city(
    city: str | None,
) -> str | None:
    if city is None:
        return None

    normalized_city = city.strip()

    if not normalized_city:
        return None

    return normalized_city


def _normalize_country_code(
    country_code: str | None,
) -> str | None:
    if country_code is None:
        return None

    normalized_country_code = country_code.strip().upper()

    if not normalized_country_code:
        return None

    return normalized_country_code


def _normalize_timezone(
    timezone: str | None,
) -> str | None:
    if timezone is None:
        return None

    normalized_timezone = timezone.strip()

    if not normalized_timezone:
        return None

    return normalized_timezone
