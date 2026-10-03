from typing import TypedDict

import geonamescache  # type: ignore
from timezonefinder import TimezoneFinder


_GEONAMES = geonamescache.GeonamesCache(min_city_population=500)
_TIMEZONE_FINDER = TimezoneFinder(in_memory=True)


class TimezoneResolution(TypedDict):
    timezone: str
    city: str | None
    country_code: str | None


class _CityData(TypedDict):
    name: str
    countrycode: str
    population: int
    latitude: float
    longitude: float
    timezone: str


class _CityCandidate(TypedDict):
    name: str
    country_code: str
    population: int
    latitude: float
    longitude: float
    timezone: str


def resolve_timezone(
    city: str | None = None,
    country_code: str | None = None,
) -> TimezoneResolution:
    """
    Resolves a geographic location to an IANA timezone.

    The resolver accepts either a city, a country, or both.

    City resolution:

        resolve_timezone(city="London", country_code="GB")
        -> Europe/London

    If only a city is provided, the city name does not have to be globally
    unique. All matching cities are considered and ranked by:

    1. Exact city name match.
    2. Population.

    This allows a common query such as:

        resolve_timezone(city="London")
        -> Europe/London

    instead of treating the multiple cities named "London" as an error.

    For example, "London" in Great Britain has an exact name match and a
    much larger population than other cities named "London", so it is
    selected as the most likely intended location.

    If a country code is provided together with the city, candidates from
    other countries are excluded:

        resolve_timezone(city="London", country_code="CA")
        -> America/Toronto

    Country-only resolution:

        resolve_timezone(country_code="JP")
        -> Asia/Tokyo

    If a country has exactly one timezone, that timezone is returned.

    If a country has multiple timezones, the resolver does not arbitrarily
    select one because the country alone is insufficient to determine the
    local time:

        resolve_timezone(country_code="US")
        -> ValueError

    In that case, a more specific location such as a city or explicit
    timezone is required.

    The result contains the resolved timezone together with the selected
    city and country code when a city was used.
    """

    normalized_city = _normalize_city(city)
    normalized_country_code = _normalize_country_code(country_code)

    if normalized_city is None and normalized_country_code is None:
        raise ValueError(
            "Either city or country_code must be provided."
        )

    if normalized_city is not None:
        return _resolve_city(
            city=normalized_city,
            country_code=normalized_country_code,
        )

    if normalized_country_code is None:
        raise ValueError(
            "Country code is required when city is not provided."
        )

    return _resolve_country(
        country_code=normalized_country_code,
    )


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


def _resolve_city(
    city: str,
    country_code: str | None,
) -> TimezoneResolution:
    candidates = _find_city_candidates(
        city=city,
        country_code=country_code,
    )

    if not candidates:
        if country_code is None:
            raise ValueError(
                f"Could not find a city matching {city!r}."
            )

        raise ValueError(
            f"Could not find city {city!r} "
            f"in country {country_code!r}."
        )

    ranked_candidates = _rank_city_candidates(
        city=city,
        candidates=candidates,
    )

    best_candidate = ranked_candidates[0]

    return {
        "timezone": best_candidate["timezone"],
        "city": best_candidate["name"],
        "country_code": best_candidate["country_code"],
    }


def _resolve_country(
    country_code: str,
) -> TimezoneResolution:
    timezones = _find_country_timezones(country_code)

    if not timezones:
        raise ValueError(
            f"Could not determine timezone for country "
            f"{country_code!r}."
        )

    if len(timezones) > 1:
        timezone_list = ", ".join(sorted(timezones))

        raise ValueError(
            f"Country {country_code!r} has multiple timezones: "
            f"{timezone_list}. "
            "A more specific location is required."
        )

    return {
        "timezone": next(iter(timezones)),
        "city": None,
        "country_code": country_code,
    }


def _find_city_candidates(
    city: str,
    country_code: str | None,
) -> list[_CityCandidate]:
    city_data_list = _GEONAMES.search_cities(
        city,
        case_sensitive=False,
        contains_search=False,
    )

    candidates: list[_CityCandidate] = []

    for city_data in city_data_list:
        candidate_country_code = city_data["countrycode"].upper()

        if (
            country_code is not None
            and candidate_country_code != country_code
        ):
            continue

        timezone = _get_city_timezone(city_data)

        if timezone is None:
            continue

        candidates.append(
            {
                "name": city_data["name"],
                "country_code": candidate_country_code,
                "population": city_data["population"],
                "latitude": city_data["latitude"],
                "longitude": city_data["longitude"],
                "timezone": timezone,
            }
        )

    return candidates


def _get_city_timezone(
    city_data: _CityData,
) -> str | None:
    timezone = city_data["timezone"]

    if timezone:
        return timezone

    return _TIMEZONE_FINDER.timezone_at(
        lng=city_data["longitude"],
        lat=city_data["latitude"],
    )


def _rank_city_candidates(
    city: str,
    candidates: list[_CityCandidate],
) -> list[_CityCandidate]:
    normalized_city = city.casefold()

    return sorted(
        candidates,
        key=lambda candidate: (
            _name_match_score(
                normalized_city,
                candidate["name"],
            ),
            candidate["population"],
        ),
        reverse=True,
    )


def _name_match_score(
    normalized_city: str,
    candidate_name: str,
) -> int:
    normalized_candidate_name = candidate_name.casefold()

    if normalized_candidate_name == normalized_city:
        return 2

    return 1


def _find_country_timezones(
    country_code: str,
) -> set[str]:
    city_data = _GEONAMES.get_cities()

    timezones: set[str] = set()

    for city in city_data.values():
        candidate_country_code = city["countrycode"].upper()

        if candidate_country_code != country_code:
            continue

        timezone = _get_city_timezone(city)

        if timezone is not None:
            timezones.add(timezone)

    return timezones


if __name__ == "__main__":
    print(resolve_timezone(city="ロンドン"))
    print(resolve_timezone(city="Лондон"))
    print(resolve_timezone(city="London"))
    print(resolve_timezone(city="London", country_code="GB"))
    print(resolve_timezone(city="London", country_code="CA"))
    print(resolve_timezone(country_code="JP"))
    print(resolve_timezone(city="Москва"))
    print(resolve_timezone(city="Томск"))
    print(resolve_timezone(city="Tomsk"))
    print(resolve_timezone(city="Санкт-Петербург"))
    print(resolve_timezone(city="Saint Petersburg"))


    try:
        print(resolve_timezone(country_code="US"))
    except ValueError as error:
        print(error)
        