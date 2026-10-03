from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from assistant.assistant_config import ASSISTANT_CONFIG
from tools.datetime.datetime_tools import get_datetime


def test_get_datetime_with_city_and_country() -> None:
    result = get_datetime("London", "GB")

    assert result["timezone"] == "Europe/London"
    assert result["date"]
    assert result["time"]
    assert result["datetime"]
    assert result["utc_offset"]

    assert result["weekday"] in range(1, 8)
    assert result["day"] in range(1, 32)
    assert result["month"] in range(1, 13)
    assert result["year"] >= 2026


def test_get_datetime_with_city_without_country() -> None:
    result = get_datetime("London")

    assert result["timezone"] == "Europe/London"


def test_get_datetime_with_explicit_timezone() -> None:
    result = get_datetime(timezone="Europe/London")

    assert result["timezone"] == "Europe/London"


def test_get_datetime_timezone_has_priority() -> None:
    result = get_datetime(
        city="London",
        country_code="GB",
        timezone="America/New_York",
    )

    assert result["timezone"] == "America/New_York"


def test_get_datetime_without_location_uses_user_timezone() -> None:
    user_timezone = ASSISTANT_CONFIG.user.timezone

    if not user_timezone:
        pytest.skip("User timezone is not configured.")

    result = get_datetime()

    assert result["timezone"] == user_timezone


def test_get_datetime_matches_timezone() -> None:
    result = get_datetime("London", "GB")

    timezone_name = result["timezone"]
    current_datetime = datetime.now(ZoneInfo(timezone_name))

    assert result["date"] == current_datetime.strftime("%Y-%m-%d")
    assert result["time"] == current_datetime.strftime("%H:%M:%S")
    assert result["utc_offset"] == current_datetime.strftime("%z")


def test_get_datetime_result_datetime_is_valid() -> None:
    result = get_datetime("London", "GB")

    parsed_datetime = datetime.fromisoformat(
        result["datetime"]
    )

    assert parsed_datetime.tzinfo is not None
    assert parsed_datetime.strftime("%Y-%m-%d") == result["date"]
    assert parsed_datetime.strftime("%H:%M:%S") == result["time"]


def test_get_datetime_result_contains_correct_calendar_values() -> None:
    result = get_datetime("London", "GB")

    parsed_datetime = datetime.fromisoformat(
        result["datetime"]
    )

    assert result["weekday"] == parsed_datetime.isoweekday()
    assert result["day"] == parsed_datetime.day
    assert result["month"] == parsed_datetime.month
    assert result["year"] == parsed_datetime.year
