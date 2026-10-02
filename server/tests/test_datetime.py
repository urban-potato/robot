from datetime import datetime
from zoneinfo import ZoneInfo

import pytest

from assistant.assistant_config import ASSISTANT_CONFIG
from tools.datetime.helpers.resolve_timezone import resolve_timezone
from tools.datetime.datetime_tools import get_datetime


def test_resolve_timezone_with_country() -> None:
    assert resolve_timezone("London", "GB") == "Europe/London"


def test_resolve_timezone_without_country_raises_for_ambiguous_city() -> None:
    with pytest.raises(
        ValueError,
        match="Location 'London' is ambiguous",
    ):
        resolve_timezone("London")


def test_resolve_timezone_normalizes_input() -> None:
    assert resolve_timezone("  London  ", " gb ") == "Europe/London"


def test_resolve_timezone_unknown_city() -> None:
    with pytest.raises(
        ValueError,
        match="Could not find a city matching",
    ):
        resolve_timezone("ThisCityDoesNotExist")


def test_resolve_timezone_unknown_city_in_country() -> None:
    with pytest.raises(
        ValueError,
        match="Could not find city",
    ):
        resolve_timezone("London", "ZZ")


def test_resolve_timezone_empty_city() -> None:
    with pytest.raises(
        ValueError,
        match="City cannot be empty",
    ):
        resolve_timezone("")


def test_get_datetime_with_city() -> None:
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


def test_get_datetime_matches_timezone() -> None:
    result = get_datetime("London", "GB")

    timezone_name = result["timezone"]
    current_datetime = datetime.now(ZoneInfo(str(timezone_name)))

    assert result["date"] == current_datetime.strftime("%Y-%m-%d")
    assert result["utc_offset"] == current_datetime.strftime("%z")


def test_get_datetime_without_city_uses_user_timezone() -> None:
    user_timezone = ASSISTANT_CONFIG.user.timezone

    if not user_timezone:
        pytest.skip("User timezone is not configured.")

    result = get_datetime()

    assert result["timezone"] == user_timezone


def test_get_datetime_result_datetime_is_valid() -> None:
    result = get_datetime("London", "GB")

    parsed_datetime = datetime.fromisoformat(
        str(result["datetime"])
    )

    assert parsed_datetime.tzinfo is not None
    assert parsed_datetime.strftime("%Y-%m-%d") == result["date"]
    assert parsed_datetime.strftime("%H:%M:%S") == result["time"]