from dataclasses import dataclass
from typing import Any

from .config import ANDROID_VARIANTS, FLUTTER_VARIANTS, LONDON_CITY_VARIANTS, PYTHON_VARIANTS, TOKYO_CITY_VARIANTS, UBUNTU_VARIANTS, USER_CITY_VARIANTS


@dataclass(frozen=True)
class ToolRouteTest:
    message: str
    expected_tool: str | None
    expected_arguments: dict[str, Any]
    expected_clarification: bool
    expected_query_requirements: tuple[
        tuple[str, ...],
        ...,
    ] = ()


TEST_GROUPS = [
    (
        "Stable knowledge",
        [
            ToolRouteTest(
                "Что такое рекурсия?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает рекурсия?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Объясни рекурсию.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое TCP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает TCP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Объясни TCP.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое указатель в C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает указатель в C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое Python?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает сборщик мусора?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое HTTP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает HTTP?",
                None,
                {},
                False,
            ),
        ],
    ),

    (
        "Current information",
        [
            ToolRouteTest(
                "Какая сейчас последняя версия Python?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая сейчас последняя версия пайтона?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия Python?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая сейчас версия Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия флаттер?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия Флаттера?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая сейчас версия ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас версия esp idf?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая последняя версия ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас версия Ubuntu?",
                "web_search",
                {},
                False,
                (
                    UBUNTU_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия Ubuntu?",
                "web_search",
                {},
                False,
                (
                    UBUNTU_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия Убунту?",
                "web_search",
                {},
                False,
                (
                    UBUNTU_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая сейчас версия Android?",
                "web_search",
                {},
                False,
                (
                    ANDROID_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая сейчас последняя версия андроид?",
                "web_search",
                {},
                False,
                (
                    ANDROID_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия Android?",
                "web_search",
                {},
                False,
                (
                    ANDROID_VARIANTS,
                )
            ),
            ToolRouteTest(
                "Какая последняя версия андроида?",
                "web_search",
                {},
                False,
                (
                    ANDROID_VARIANTS,
                )
            ),
        ],
    ),

    (
        "Current vs stable",
        [
            ToolRouteTest(
                "Как работает Python?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает пайтон?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает Flutter?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Объясни, как работает Флаттер?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает ESP-IDF?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает TCP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает Git?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое Python?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое Flutter?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое ESP-IDF?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое функция?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое стек вызовов?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое указатель?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое ссылка в C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое процесс?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое поток?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает сборщик мусора?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает Git?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает TCP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как работает HTTP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас рекомендуемая версия Python?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас рекомендуемая версия Flutter?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас рекомендуемая версия ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас версия Git?",
                "web_search",
                {},
                False,
            ),
        ],
    ),

    (
        "Explicit web search",
        [
            ToolRouteTest(
                "Поищи информацию о Python.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Поищи информацию о питоне, который язык программирования.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Поищи информацию о Flutter.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Поищи информацию об ESP-IDF.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Поищи информацию о C++.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Поищи информацию о TCP.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Поищи информацию о рекурсии.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Найди документацию Python.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Найди документацию Flutter.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Найди документацию флаттера.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Найди документацию ESP-IDF.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Найди информацию об указателях в C++.",
                "web_search",
                {},
                False,
            ),
        ],
    ),

    (
        "Specific web page",
        [
            ToolRouteTest(
                "Что написано на https://example.com?",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Прочитай https://example.com",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Что находится на странице https://example.com?",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Расскажи, о чём страница https://example.com",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Проверь содержимое https://example.com",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Что говорит https://example.com?",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
        ],
    ),

    (
        "Current date and time",
        [
            ToolRouteTest(
                "Который сейчас час?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Который час?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Сколько времени?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Сколько сейчас времени?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас дата?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Какое сегодня число?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Какой сегодня день недели?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Какой сегодня день?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Сегодня выходной?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас дата и время?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Что сейчас за дата?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Какой сейчас месяц?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Напомни, какой месяц.",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Какой сейчас год?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Напомни какой год",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Лондоне?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Сколько времени в Лондоне?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Который сейчас час в Лондоне?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Который час в Лондоне?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Время в Лондоне?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас дата в Лондоне?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Какой сегодня день недели в Лондоне?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Токио?",
                "get_datetime",
                {"city": "Tokyo"},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас дата в Токио?",
                "get_datetime",
                {"city": "Tokyo"},
                False,
            ),
            ToolRouteTest(
                "Какой сегодня день недели в Токио?",
                "get_datetime",
                {"city": "Tokyo"},
                False,
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Лондоне Великобритания?",
                "get_datetime",
                {
                    "city": "London",
                    "country_code": "GB",
                },
                False,
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Токио Япония?",
                "get_datetime",
                {
                    "city": "Tokyo",
                    "country_code": "JP",
                },
                False,
            ),
        ],
    ),

    (
        "Personal and conversational",
        [
            ToolRouteTest(
                "Какой у тебя любимый цвет?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Какой цвет тебе нравится?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Какой цвет ты любишь?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что ты любишь?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Как дела?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Чем ты сейчас занимаешься?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Ты любишь музыку?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Расскажи о себе.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Какие у тебя интересы?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что тебе нравится?",
                None,
                {},
                False,
            ),
        ],
    ),

    (
        "Stable programming",
        [
            ToolRouteTest(
                "Что такое класс в C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое объект в C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое указатель?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое ссылка в C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Чем указатель отличается от ссылки?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое функция?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое рекурсия?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое стек вызовов?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что такое процесс?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Чем процесс отличается от потока?",
                None,
                {},
                False,
            ),
        ],
    ),

    (
        "Current programming information",
        [
            ToolRouteTest(
                "Какая сейчас версия C++?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая последняя версия C++?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая последняя версия си плюс плюс?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас версия GCC?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая последняя версия GCC?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас версия Clang?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая последняя версия Clang?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас версия Git?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая сейчас версия гит?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая последняя версия Git?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Какая последняя версия гита?",
                "web_search",
                {},
                False,
            ),
        ],
    ),

    (
        "Search wording without explicit web mention",
        [
            ToolRouteTest(
                "Узнай последнюю версию Python.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Узнай текущую версию Flutter.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Узнай текущую версию ESP-IDF.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Узнай, сколько сейчас стоит доллар.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Узнай последние изменения в Python.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Что нового во флаттере?",
                "web_search",
                {},
                False,
            ),
        ],
    ),

    (
        "Location-specific web search",
        [
            ToolRouteTest(
                "Проверь погоду на завтра.",
                "web_search",
                {},
                False,
                (
                    (
                        "weather",
                        "погода",
                        "forecast",
                        "прогноз",
                    ),
                    USER_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Какая погода сегодня?",
                "web_search",
                {},
                False,
                (
                    (
                        "weather",
                        "погода",
                        "forecast",
                        "прогноз",
                    ),
                    USER_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Будет ли завтра дождь?",
                "web_search",
                {},
                False,
                (
                    (
                        "rain",
                        "дождь",
                        "rainfall",
                    ),
                    USER_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Какая температура сейчас?",
                "web_search",
                {},
                False,
                (
                    (
                        "temperature",
                        "температура",
                        "degrees",
                        "градус",
                    ),
                    USER_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Какая погода завтра в Лондоне?",
                "web_search",
                {},
                False,
                (
                    (
                        "weather",
                        "погода",
                        "forecast",
                        "прогноз",
                    ),
                    LONDON_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Будет ли завтра дождь в Токио?",
                "web_search",
                {},
                False,
                (
                    (
                        "rain",
                        "дождь",
                        "rainfall",
                    ),
                    TOKYO_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Какая температура сейчас в Лондоне?",
                "web_search",
                {},
                False,
                (
                    (
                        "temperature",
                        "температура",
                        "degrees",
                        "градус",
                    ),
                    LONDON_CITY_VARIANTS,
                ),
            ),
        ],
    ),

    (
        "Potentially ambiguous",
        [
            ToolRouteTest(
                "Расскажи про Python.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Расскажи про Flutter.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Что нового в Python?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Что нового в Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Что сейчас происходит с Python?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Что сейчас происходит с Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Что нового в ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Расскажи про ESP32.",
                None,
                {},
                False,
            ),
        ],
    ),

    (
        "Clarification",
        [
            ToolRouteTest(
                "Узнай расписание на сегодня.",
                None,
                {},
                True,
            ),
            ToolRouteTest(
                "Проверь, доступен ли сейчас этот сервис.",
                None,
                {},
                True,
            ),
            ToolRouteTest(
                "Проверь, сколько стоит.",
                None,
                {},
                True,
            ),
            ToolRouteTest(
                "Узнай последние новости.",
                "web_search",
                {},
                False,
            ),
        ],
    ),

    (
        "Resolved external requests",
        [
            ToolRouteTest(
                "Проверь погоду на завтра в Лондоне.",
                "web_search",
                {},
                False,
                (
                    (
                        "weather",
                        "погода",
                        "forecast",
                        "прогноз",
                    ),
                    LONDON_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Проверь погоду на завтра в Токио.",
                "web_search",
                {},
                False,
                (
                    (
                        "weather",
                        "погода",
                        "forecast",
                        "прогноз",
                    ),
                    TOKYO_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Проверь, доступен ли сейчас GitHub.",
                "web_search",
                {},
                False,
                (
                    (
                        "GitHub",
                        "гитхаб",
                    ),
                ),
            ),
            ToolRouteTest(
                "Поищи информацию о рекурсии.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Поищи информацию о TCP.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Найди документацию Python.",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Поищи, что такое указатели в C++.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Узнай, сколько сейчас стоит доллар.",
                "web_search",
                {},
                False,
            ),
        ],
    ),
]
