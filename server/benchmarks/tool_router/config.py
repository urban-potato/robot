from assistant.types import UserConfig


USER_CONFIG = UserConfig(
    name="Joan",
    gender="Female",
    city="Saint Petersburg",
    country_code="RU",
    timezone="Europe/Moscow",
)

USER_CITY_VARIANTS: tuple[str, ...] = (
    USER_CONFIG.city,
    "St Petersburg",
    "Санкт-Петербург",
    "Санкт Петербург",
    "Петербург",
    "Питер",
)

TOKYO_CITY_VARIANTS: tuple[str, ...] = (
    "Tokyo",
    "Токио",
    "東京",
)

LONDON_CITY_VARIANTS: tuple[str, ...] = (
    "London",
    "Лондон",
)

PYTHON_VARIANTS: tuple[str, ...] = (
    "python",
    "питон",
    "пайтон",
)

FLUTTER_VARIANTS: tuple[str, ...] = (
    "flutter",
    "флаттер",
)

UBUNTU_VARIANTS: tuple[str, ...] = (
    "ubuntu",
    "убунту",
)

ANDROID_VARIANTS: tuple[str, ...] = (
    "android",
    "андроид",
)
