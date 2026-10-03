import pytest

from tools.datetime.helpers.resolve_timezone import resolve_timezone


def test_resolve_timezone_with_city_and_country() -> None:
    result = resolve_timezone("London", "GB")

    assert result["timezone"] == "Europe/London"
    assert result["city"] == "London"
    assert result["country_code"] == "GB"


def test_resolve_timezone_with_city_without_country() -> None:
    result = resolve_timezone("London")

    assert result["timezone"] == "Europe/London"
    assert result["city"] == "London"
    assert result["country_code"] == "GB"


def test_resolve_timezone_normalizes_input() -> None:
    result = resolve_timezone("  London  ", " gb ")

    assert result["timezone"] == "Europe/London"
    assert result["city"] == "London"
    assert result["country_code"] == "GB"


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


def test_resolve_timezone_with_ambiguous_country_raises() -> None:
    with pytest.raises(
        ValueError,
        match="multiple timezones",
    ):
        resolve_timezone(country_code="US")


def test_resolve_timezone_empty_inputs_raise() -> None:
    with pytest.raises(
        ValueError,
        match="Either city or country_code must be provided",
    ):
        resolve_timezone("", "")
