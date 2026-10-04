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
        ...
    ] = ()


TEST_GROUPS = [
    (
        "Stable knowledge",
        [
            ToolRouteTest(
                "What is recursion?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does recursion work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Explain recursion.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is TCP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does TCP work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Explain TCP.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a pointer in C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does a pointer in C++ work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is Python?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does garbage collection work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is HTTP?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does HTTP work?",
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
                "What is the latest version of Python right now?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Python right now?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Python?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the current version of Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the current version of ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current version of ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the latest version of ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current version of Ubuntu?",
                "web_search",
                {},
                False,
                (
                    UBUNTU_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Ubuntu?",
                "web_search",
                {},
                False,
                (
                    UBUNTU_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Ubuntu?",
                "web_search",
                {},
                False,
                (
                    UBUNTU_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the current version of Android?",
                "web_search",
                {},
                False,
                (
                    ANDROID_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Android right now?",
                "web_search",
                {},
                False,
                (
                    ANDROID_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Android?",
                "web_search",
                {},
                False,
                (
                    ANDROID_VARIANTS,
                )
            ),
            ToolRouteTest(
                "What is the latest version of Android?",
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
                "How does Python work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does Python work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does Flutter work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Explain how Flutter works?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does ESP-IDF work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does TCP work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does Git work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is Python?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is Flutter?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is ESP-IDF?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a function?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a call stack?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a pointer?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a reference in C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a process?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a thread?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does garbage collection work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does Git work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does TCP work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How does HTTP work?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is the currently recommended version of Python?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the currently recommended version of Flutter?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the currently recommended version of ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current version of Git?",
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
                "Search for information about Python.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Search for information about Python, the programming language.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Search for information about Flutter.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Search for information about ESP-IDF.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Search for information about C++.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Search for information about TCP.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Search for information about recursion.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find Python documentation.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find Flutter documentation.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find Flutter documentation.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find ESP-IDF documentation.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find information about pointers in C++.",
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
                "What is written on https://example.com?",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Read https://example.com",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "What is on the page https://example.com?",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Tell me what the page https://example.com is about",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "Check the contents of https://example.com",
                "web_page_read",
                {"url": "https://example.com"},
                False,
            ),
            ToolRouteTest(
                "What does https://example.com say?",
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
                "What time is it right now?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What time is it?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What time is it?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What time is it right now?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What is today's date?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What is today's date?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What day of the week is it today?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What day is it today?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Is today a weekend?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current date and time?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What is today's date?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What month is it?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Remind me what month it is.",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What year is it?",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "Remind me what year it is.",
                "get_datetime",
                {},
                False,
            ),
            ToolRouteTest(
                "What time is it in London right now?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "What time is it in London?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "What time is it in London right now?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "What time is it in London?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "Time in London?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "What is the current date in London?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "What day of the week is it today in London?",
                "get_datetime",
                {"city": "London"},
                False,
            ),
            ToolRouteTest(
                "What time is it in Tokyo right now?",
                "get_datetime",
                {"city": "Tokyo"},
                False,
            ),
            ToolRouteTest(
                "What is the current date in Tokyo?",
                "get_datetime",
                {"city": "Tokyo"},
                False,
            ),
            ToolRouteTest(
                "What day of the week is it today in Tokyo?",
                "get_datetime",
                {"city": "Tokyo"},
                False,
            ),
            ToolRouteTest(
                "What time is it in London, United Kingdom?",
                "get_datetime",
                {
                    "city": "London",
                    "country_code": "GB",
                },
                False,
            ),
            ToolRouteTest(
                "What time is it in Tokyo, Japan?",
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
                "What is your favorite color?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What color do you like?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What color do you love?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What do you like?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "How are you?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What are you doing right now?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Do you like music?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Tell me about yourself.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What are your interests?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What do you like?",
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
                "What is a class in C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is an object in C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a pointer?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a reference in C++?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is the difference between a pointer and a reference?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a function?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is recursion?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a call stack?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is a process?",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What is the difference between a process and a thread?",
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
                "What is the current version of C++?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the latest version of C++?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the latest version of C++?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current version of GCC?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the latest version of GCC?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current version of Clang?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the latest version of Clang?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current version of Git?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the current version of Git?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the latest version of Git?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What is the latest version of Git?",
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
                "Find out the latest version of Python.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find out the current version of Flutter.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find out the current version of ESP-IDF.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find out how much the dollar costs right now.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find out the latest changes in Python.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "What's new in Flutter?",
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
                "Check the weather tomorrow.",
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
                "What's the weather today?",
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
                "Will it rain tomorrow?",
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
                "What's the temperature right now?",
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
                "What's the weather like tomorrow in London?",
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
                "Will it rain tomorrow in Tokyo?",
                "web_search",
                {},
                False,
                (
                    (
                        "rain",
                        "дождь",
                        "rainfall",
                        "weather",
                        "погода",
                    ),
                    TOKYO_CITY_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "What's the temperature right now in London?",
                "web_search",
                {},
                False,
                (
                    (
                        "temperature",
                        "температура",
                        "degrees",
                        "градус",
                        "weather",
                        "погода",
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
                "Tell me about Python.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "Tell me about Flutter.",
                None,
                {},
                False,
            ),
            ToolRouteTest(
                "What's new in Python?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "What's new in Flutter?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "What's happening with Python right now?",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "What's happening with Flutter right now?",
                "web_search",
                {},
                False,
                (
                    FLUTTER_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "What's new in ESP-IDF?",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Tell me about ESP32.",
                None,
                {},
                False,
            ),
        ],
    ),

    (
        "Clarification or not",
        [
            ToolRouteTest(
                "Find out today's schedule.",
                None,
                {},
                True,
            ),
            ToolRouteTest(
                "Check whether this service is currently available.",
                None,
                {},
                True,
            ),
            ToolRouteTest(
                "Check how much it costs.",
                None,
                {},
                True,
            ),
            ToolRouteTest(
                "Find out the latest news.",
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
                "Check the weather tomorrow in London.",
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
                "Check the weather tomorrow in Tokyo.",
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
                "Check whether GitHub is currently available.",
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
                "Search for information about recursion.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Search for information about TCP.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find Python documentation.",
                "web_search",
                {},
                False,
                (
                    PYTHON_VARIANTS,
                ),
            ),
            ToolRouteTest(
                "Search for information about pointers in C++.",
                "web_search",
                {},
                False,
            ),
            ToolRouteTest(
                "Find out how much the dollar costs right now.",
                "web_search",
                {},
                False,
            ),
        ],
    ),
]
