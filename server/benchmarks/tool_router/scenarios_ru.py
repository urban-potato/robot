from ai.tool_router.types import RouterArgumentName, RouterTool
from .types import ToolRouteTest

from .config import ANDROID_VARIANTS, FLUTTER_VARIANTS, LONDON_CITY_VARIANTS, PYTHON_VARIANTS, TOKYO_CITY_VARIANTS, UBUNTU_VARIANTS, USER_CITY_VARIANTS


TEST_GROUPS = [
    (
        "Stable knowledge",
        [
            ToolRouteTest(
                "Что такое рекурсия?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает рекурсия?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Объясни рекурсию.",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое TCP?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает TCP?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Объясни TCP.",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое указатель в C++?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает указатель в C++?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое Python?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает сборщик мусора?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое HTTP?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает HTTP?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
        ],
    ),

    (
        "Current information",
        [
            ToolRouteTest(
                "Какая сейчас последняя версия Python?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас последняя версия пайтона?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия Python?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас версия Flutter?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия Flutter?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия флаттер?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия Флаттера?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас версия ESP-IDF?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая сейчас версия esp idf?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая последняя версия ESP-IDF?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая сейчас версия Ubuntu?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        UBUNTU_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия Ubuntu?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        UBUNTU_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия Убунту?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        UBUNTU_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас версия Android?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        ANDROID_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас последняя версия андроид?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        ANDROID_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия Android?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        ANDROID_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая последняя версия андроида?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        ANDROID_VARIANTS,
                    ),
                },
            ),
        ],
    ),

    (
        "Current vs stable",
        [
            ToolRouteTest(
                "Как работает Python?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает пайтон?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает Flutter?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Объясни, как работает Флаттер?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает ESP-IDF?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает TCP?",
                RouterTool.DEFAULT_ASSISTANT,

            ),
            ToolRouteTest(
                "Как работает Git?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое Python?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое Flutter?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое ESP-IDF?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое функция?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое стек вызовов?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое указатель?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое ссылка в C++?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое процесс?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое поток?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает сборщик мусора?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает Git?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает TCP?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как работает HTTP?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Какая сейчас рекомендуемая версия Python?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас рекомендуемая версия Flutter?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас рекомендуемая версия ESP-IDF?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая сейчас версия Git?",
                RouterTool.WEB_SEARCH,

            ),
        ],
    ),

    (
        "Explicit web search",
        [
            ToolRouteTest(
                "Поищи информацию о Python.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Поищи информацию о питоне, который язык программирования.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Поищи информацию о Flutter.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Поищи информацию об ESP-IDF.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Поищи информацию о C++.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Поищи информацию о TCP.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Поищи информацию о рекурсии.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Найди документацию Python.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Найди документацию Flutter.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Найди документацию флаттера.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Найди документацию ESP-IDF.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Найди информацию об указателях в C++.",
                RouterTool.WEB_SEARCH,
            ),
        ],
    ),

    (
        "Specific web page",
        [
            ToolRouteTest(
                "Что написано на https://example.com?",
                RouterTool.WEB_PAGE_READ,
                expected_arguments = {RouterArgumentName.URL: "https://example.com"},
            ),
            ToolRouteTest(
                "Прочитай https://example.com",
                RouterTool.WEB_PAGE_READ,
                expected_arguments = {RouterArgumentName.URL: "https://example.com"},
            ),
            ToolRouteTest(
                "Что находится на странице https://example.com?",
                RouterTool.WEB_PAGE_READ,
                expected_arguments = {RouterArgumentName.URL: "https://example.com"},
            ),
            ToolRouteTest(
                "Расскажи, о чём страница https://example.com",
                RouterTool.WEB_PAGE_READ,
                expected_arguments = {RouterArgumentName.URL: "https://example.com"},
            ),
            ToolRouteTest(
                "Проверь содержимое https://example.com",
                RouterTool.WEB_PAGE_READ,
                expected_arguments = {RouterArgumentName.URL: "https://example.com"},
            ),
            ToolRouteTest(
                "Что говорит https://example.com?",
                RouterTool.WEB_PAGE_READ,
                expected_arguments = {RouterArgumentName.URL: "https://example.com"},
            ),
        ],
    ),

    (
        "Current date and time",
        [
            ToolRouteTest(
                "Который сейчас час?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Который час?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Сколько времени?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Сколько сейчас времени?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Какая сейчас дата?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Какое сегодня число?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Какой сегодня день недели?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Какой сегодня день?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Сегодня выходной?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Какая сейчас дата и время?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Что сейчас за дата?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Какой сейчас месяц?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Напомни, какой месяц.",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Какой сейчас год?",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Напомни какой год",
                RouterTool.GET_DATETIME,
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Лондоне?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Сколько времени в Лондоне?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Который сейчас час в Лондоне?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Который час в Лондоне?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Время в Лондоне?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас дата в Лондоне?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какой сегодня день недели в Лондоне?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Токио?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        TOKYO_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая сейчас дата в Токио?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        TOKYO_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какой сегодня день недели в Токио?",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        TOKYO_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Время Токио",
                RouterTool.GET_DATETIME,
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        TOKYO_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Лондоне Великобритания?",
                RouterTool.GET_DATETIME,
                expected_arguments = {
                    RouterArgumentName.COUNTRY_CODE: "GB",
                },
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Время Лондон Европа",
                RouterTool.GET_DATETIME,
                expected_arguments = {
                    RouterArgumentName.TIMEZONE: "Europe/London",
                },
            ),
            ToolRouteTest(
                "Сколько сейчас времени в Токио Япония?",
                RouterTool.GET_DATETIME,
                expected_arguments = {
                    RouterArgumentName.COUNTRY_CODE: "JP",
                },
                expected_argument_requirements={
                    RouterArgumentName.CITY: (
                        TOKYO_CITY_VARIANTS,
                    ),
                },
            ),
        ],
    ),

    (
        "Personal and conversational",
        [
            ToolRouteTest(
                "Какой у тебя любимый цвет?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Какой цвет тебе нравится?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Какой цвет ты любишь?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что ты любишь?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Как дела?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Чем ты сейчас занимаешься?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Ты любишь музыку?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Расскажи о себе.",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Какие у тебя интересы?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что тебе нравится?",
                RouterTool.DEFAULT_ASSISTANT,

            ),
        ],
    ),

    (
        "Stable programming",
        [
            ToolRouteTest(
                "Что такое класс в C++?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое объект в C++?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое указатель?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое ссылка в C++?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Чем указатель отличается от ссылки?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое функция?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое рекурсия?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое стек вызовов?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что такое процесс?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Чем процесс отличается от потока?",
                RouterTool.DEFAULT_ASSISTANT,
            ),
        ],
    ),

    (
        "Current programming information",
        [
            ToolRouteTest(
                "Какая сейчас версия C++?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая последняя версия C++?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая последняя версия си плюс плюс?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая сейчас версия GCC?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая последняя версия GCC?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая сейчас версия Clang?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая последняя версия Clang?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая сейчас версия Git?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая сейчас версия гит?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая последняя версия Git?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Какая последняя версия гита?",
                RouterTool.WEB_SEARCH,
            ),
        ],
    ),

    (
        "Search wording without explicit web mention",
        [
            ToolRouteTest(
                "Узнай последнюю версию Python.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Узнай текущую версию Flutter.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Узнай текущую версию ESP-IDF.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Узнай, сколько сейчас стоит доллар.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Узнай последние изменения в Python.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Что нового во флаттере?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },

            ),
        ],
    ),

    (
        "Location-specific web search",
        [
            ToolRouteTest(
                "Проверь погоду на завтра.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                        ),
                        USER_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая погода сегодня?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                        ),
                        USER_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Будет ли завтра дождь?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "rain",
                            "дождь",
                            "rainfall",
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                        ),
                        USER_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая температура сейчас?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "temperature",
                            "температура",
                            "degrees",
                            "градус",
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                        ),
                        USER_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая погода завтра в Лондоне?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                            "forecast",
                            "прогноз",
                        ),
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Будет ли завтра дождь в Токио?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "rain",
                            "дождь",
                            "rainfall",
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                            "天气",
                            "天気",
                            "予報",
                            "雨",
                        ),
                        TOKYO_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Какая температура сейчас в Лондоне?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "temperature",
                            "температура",
                            "degrees",
                            "градус",
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                        ),
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
        ],
    ),

    (
        "Potentially ambiguous",
        [
            ToolRouteTest(
                "Расскажи про Python.",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Расскажи про Flutter.",
                RouterTool.DEFAULT_ASSISTANT,
            ),
            ToolRouteTest(
                "Что нового в Python?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Что нового в Flutter?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Что сейчас происходит с Python?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Что сейчас происходит с Flutter?",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        FLUTTER_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Что нового в ESP-IDF?",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Расскажи про ESP32.",
                RouterTool.DEFAULT_ASSISTANT,

            ),
        ],
    ),

    (
        "Clarification or not",
        [
            ToolRouteTest(
                "Узнай расписание на сегодня.",
                RouterTool.CLARIFICATION,
            ),
            ToolRouteTest(
                "Проверь, доступен ли сейчас.",
                RouterTool.CLARIFICATION,
            ),
            ToolRouteTest(
                "Проверь, доступен ли сейчас этот сервис.",
                RouterTool.CLARIFICATION,
            ),
            ToolRouteTest(
                "Проверь, сколько стоит.",
                RouterTool.CLARIFICATION,
            ),
            ToolRouteTest(
                "Что такое?",
                RouterTool.CLARIFICATION,
            ),
            ToolRouteTest(
                "Объясни мне",
                RouterTool.CLARIFICATION,
            ),
            ToolRouteTest(
                "Узнай последние новости.",
                RouterTool.WEB_SEARCH,
            ),
        ],
    ),

    (
        "Resolved external requests",
        [
            ToolRouteTest(
                "Проверь погоду на завтра в Лондоне.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                        ),
                        LONDON_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Проверь погоду на завтра в Токио.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "weather",
                            "погода",
                            "forecast",
                            "прогноз",
                            "天气",
                            "天気",
                            "予報",
                        ),
                        TOKYO_CITY_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Проверь, доступен ли сейчас GitHub.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        (
                            "GitHub",
                            "гитхаб",
                        ),
                    ),
                },
            ),
            ToolRouteTest(
                "Поищи информацию о рекурсии.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Поищи информацию о TCP.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Найди документацию Python.",
                RouterTool.WEB_SEARCH,
                expected_argument_requirements = {
                    RouterArgumentName.QUERY: (
                        PYTHON_VARIANTS,
                    ),
                },
            ),
            ToolRouteTest(
                "Поищи, что такое указатели в C++.",
                RouterTool.WEB_SEARCH,
            ),
            ToolRouteTest(
                "Узнай, сколько сейчас стоит доллар.",
                RouterTool.WEB_SEARCH,
            ),
        ],
    ),
]
