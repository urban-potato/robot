import geonamescache  # type: ignore
from timezonefinder import TimezoneFinder

_GEONAMES = geonamescache.GeonamesCache(min_city_population=500)
_TIMEZONE_FINDER = TimezoneFinder(in_memory=True)


def resolve_timezone(
    city: str,
    country_code: str | None = None,
) -> str:
    normalized_city = city.strip()

    if not normalized_city:
        raise ValueError("City cannot be empty.")

    normalized_country_code = (
        country_code.strip().upper()
        if country_code is not None
        else None
    )

    cities = _GEONAMES.search_cities(
        normalized_city,
        case_sensitive=False,
        contains_search=False,
    )

    if normalized_country_code is not None:
        cities = [
            city_data
            for city_data in cities
            if city_data["countrycode"].upper()
            == normalized_country_code
        ]

    if not cities:
        if normalized_country_code is None:
            raise ValueError(
                f"Could not find a city matching {city!r}."
            )

        raise ValueError(
            f"Could not find city {city!r} "
            f"in country {normalized_country_code!r}."
        )

    timezones: set[str] = set()

    for city_data in cities:
        timezone = _TIMEZONE_FINDER.timezone_at(
            lng=city_data["longitude"],
            lat=city_data["latitude"],
        )

        if timezone is not None:
            timezones.add(timezone)

    if not timezones:
        raise ValueError(
            f"Could not determine timezone for {city!r}."
        )

    if len(timezones) > 1:
        city_names = sorted(
            {city_data["name"] for city_data in cities}
        )

        raise ValueError(
            f"Location {city!r} is ambiguous. "
            f"Possible matches: {', '.join(city_names)}."
        )

    return next(iter(timezones))
