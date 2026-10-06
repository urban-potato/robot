# from ai.tool_router.types import RouterArgumentName, RouterTool
# from .types import ToolRouteTest

# from .config import ANDROID_VARIANTS, FLUTTER_VARIANTS, LONDON_CITY_VARIANTS, PYTHON_VARIANTS, TOKYO_CITY_VARIANTS, UBUNTU_VARIANTS, USER_CITY_VARIANTS


# TEST_GROUPS = [
#     (
#         "Stable knowledge",
#         [
#             ToolRouteTest(
#                 "What is recursion?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does recursion work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "Explain recursion.",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is TCP?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does TCP work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "Explain TCP.",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a pointer in C++?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does a pointer in C++ work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is Python?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does garbage collection work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is HTTP?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does HTTP work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#         ],
#     ),

#     (
#         "Current information",
#         [
#             ToolRouteTest(
#                 "What is the latest version of Python?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Python right now?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 )
#             ),
#             ToolRouteTest(
#                 "What is the latest Python version?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the current version of Flutter?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Flutter?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Flutter?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Flutter?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the current version of ESP-IDF?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the current version of ESP-IDF?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the latest version of ESP-IDF?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the current version of Ubuntu?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     UBUNTU_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Ubuntu?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     UBUNTU_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Ubuntu?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     UBUNTU_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the current version of Android?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     ANDROID_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Android?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     ANDROID_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Android?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     ANDROID_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Android?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     ANDROID_VARIANTS,
#                 ),
#             ),
#         ],
#     ),

#     (
#         "Current vs stable",
#         [
#             ToolRouteTest(
#                 "How does Python work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does Python work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does Flutter work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "Explain how Flutter works.",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does ESP-IDF work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does TCP work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does Git work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is Python?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is Flutter?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is ESP-IDF?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a function?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is the call stack?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a pointer?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a reference in C++?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a process?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a thread?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does garbage collection work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does Git work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does TCP work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How does HTTP work?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is the currently recommended version of Python?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the currently recommended version of Flutter?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What is the currently recommended version of ESP-IDF?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the current version of Git?",
#                 RouterTool.WEB_SEARCH,
#             ),
#         ],
#     ),

#     (
#         "Explicit web search",
#         [
#             ToolRouteTest(
#                 "Search for information about Python.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Search for information about Python, the programming language.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Search for information about Flutter.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Search for information about ESP-IDF.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Search for information about C++.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Search for information about TCP.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Search for information about recursion.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Find Python documentation.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Find Flutter documentation.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Find Flutter documentation.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Find ESP-IDF documentation.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Find information about pointers in C++.",
#                 RouterTool.WEB_SEARCH,
#             ),
#         ],
#     ),

#     (
#         "Specific web page",
#         [
#             ToolRouteTest(
#                 "What is written on https://example.com?",
#                 RouterTool.WEB_PAGE_READ,
#                 expected_arguments = {RouterArgumentName.URL: "https://example.com"},
#             ),
#             ToolRouteTest(
#                 "Read https://example.com",
#                 RouterTool.WEB_PAGE_READ,
#                 expected_arguments = {RouterArgumentName.URL: "https://example.com"},
#             ),
#             ToolRouteTest(
#                 "What is on the page https://example.com?",
#                 RouterTool.WEB_PAGE_READ,
#                 expected_arguments = {RouterArgumentName.URL: "https://example.com"},
#             ),
#             ToolRouteTest(
#                 "Tell me what the page https://example.com is about.",
#                 RouterTool.WEB_PAGE_READ,
#                 expected_arguments = {RouterArgumentName.URL: "https://example.com"},
#             ),
#             ToolRouteTest(
#                 "Check the contents of https://example.com",
#                 RouterTool.WEB_PAGE_READ,
#                 expected_arguments = {RouterArgumentName.URL: "https://example.com"},
#             ),
#             ToolRouteTest(
#                 "What does https://example.com say?",
#                 RouterTool.WEB_PAGE_READ,
#                 expected_arguments = {RouterArgumentName.URL: "https://example.com"},
#             ),
#         ],
#     ),

#     (
#         "Current date and time",
#         [
#             ToolRouteTest(
#                 "What time is it right now?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What time is it?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What time is it?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What time is it right now?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What is today's date?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What is today's date?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What day of the week is it today?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What day is it today?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "Is today a weekend?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What is the current date and time?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What date is it right now?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What month is it?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "Remind me what month it is.",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What year is it?",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "Remind me what year it is.",
#                 RouterTool.GET_DATETIME,
#             ),
#             ToolRouteTest(
#                 "What time is it in London right now?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "London"},
#             ),
#             ToolRouteTest(
#                 "What time is it in London?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "London"},
#             ),
#             ToolRouteTest(
#                 "What hour is it in London right now?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "London"},
#             ),
#             ToolRouteTest(
#                 "What time is it in London?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "London"},
#             ),
#             ToolRouteTest(
#                 "Time in London?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "London"},
#             ),
#             ToolRouteTest(
#                 "What is the current date in London?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "London"},
#             ),
#             ToolRouteTest(
#                 "What day of the week is it in London today?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "London"},
#             ),
#             ToolRouteTest(
#                 "What time is it in Tokyo right now?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "Tokyo"},
#             ),
#             ToolRouteTest(
#                 "What is the current date in Tokyo?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "Tokyo"},
#             ),
#             ToolRouteTest(
#                 "What day of the week is it in Tokyo today?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {RouterArgumentName.CITY: "Tokyo"},
#             ),
#             ToolRouteTest(
#                 "What time is it in London, United Kingdom?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {
#                     RouterArgumentName.CITY: "London",
#                     RouterArgumentName.COUNTRY_CODE: "GB",
#                 },
#             ),
#             ToolRouteTest(
#                 "What time is it in Tokyo, Japan?",
#                 RouterTool.GET_DATETIME,
#                 expected_arguments = {
#                     RouterArgumentName.CITY: "Tokyo",
#                     RouterArgumentName.COUNTRY_CODE: "JP",
#                 },
#             ),
#         ],
#     ),

#     (
#         "Personal and conversational",
#         [
#             ToolRouteTest(
#                 "What is your favorite color?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What color do you like?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What color do you love?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What do you like?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "How are you?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What are you doing right now?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "Do you like music?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "Tell me about yourself.",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What are your interests?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What do you like?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#         ],
#     ),

#     (
#         "Stable programming",
#         [
#             ToolRouteTest(
#                 "What is a class in C++?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is an object in C++?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a pointer?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a reference in C++?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is the difference between a pointer and a reference?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a function?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is recursion?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is the call stack?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is a process?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What is the difference between a process and a thread?",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#         ],
#     ),

#     (
#         "Current programming information",
#         [
#             ToolRouteTest(
#                 "What is the current version of C++?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the latest version of C++?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the latest version of C++?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the current version of GCC?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the latest version of GCC?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the current version of Clang?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Clang?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the current version of Git?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the current version of Git?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Git?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "What is the latest version of Git?",
#                 RouterTool.WEB_SEARCH,
#             ),
#         ],
#     ),

#     (
#         "Search wording without explicit web mention",
#         [
#             ToolRouteTest(
#                 "Find out the latest version of Python.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Find out the current version of Flutter.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Find out the current version of ESP-IDF.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Find out how much the dollar costs right now.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Find out the latest changes in Python.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's new in Flutter?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#         ],
#     ),

#     (
#         "Location-specific web search",
#         [
#             ToolRouteTest(
#                 "Check the weather for tomorrow.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "weather",
#                         "погода",
#                         "forecast",
#                         "прогноз",
#                     ),
#                     USER_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's the weather like today?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "weather",
#                         "погода",
#                         "forecast",
#                         "прогноз",
#                     ),
#                     USER_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Will it rain tomorrow?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "rain",
#                         "дождь",
#                         "rainfall",
#                     ),
#                     USER_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's the temperature right now?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "temperature",
#                         "температура",
#                         "degrees",
#                         "градус",
#                     ),
#                     USER_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's the weather like tomorrow in London?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "weather",
#                         "погода",
#                         "forecast",
#                         "прогноз",
#                     ),
#                     LONDON_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Will it rain tomorrow in Tokyo?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "rain",
#                         "дождь",
#                         "rainfall",
#                         "weather",
#                         "погода",
#                     ),
#                     TOKYO_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's the temperature in London right now?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "temperature",
#                         "температура",
#                         "degrees",
#                         "градус",
#                         "weather",
#                         "погода",
#                     ),
#                     LONDON_CITY_VARIANTS,
#                 ),
#             ),
#         ],
#     ),

#     (
#         "Potentially ambiguous",
#         [
#             ToolRouteTest(
#                 "Tell me about Python.",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "Tell me about Flutter.",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#             ToolRouteTest(
#                 "What's new in Python?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's new in Flutter?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's happening with Python right now?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's happening with Flutter right now?",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     FLUTTER_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "What's new in ESP-IDF?",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Tell me about ESP32.",
#                 RouterTool.DEFAULT_ASSISTANT,
#             ),
#         ],
#     ),

#     (
#         "Clarification or not",
#         [
#             ToolRouteTest(
#                 "Find out today's schedule.",
#                 RouterTool.CLARIFICATION,
#             ),
#             ToolRouteTest(
#                 "Check whether this service is currently available.",
#                 RouterTool.CLARIFICATION,
#             ),
#             ToolRouteTest(
#                 "Check how much it costs.",
#                 RouterTool.CLARIFICATION,
#             ),
#             ToolRouteTest(
#                 "Find out the latest news.",
#                 RouterTool.WEB_SEARCH,
#             ),
#         ],
#     ),

#     (
#         "Resolved external requests",
#         [
#             ToolRouteTest(
#                 "Check the weather for tomorrow in London.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "weather",
#                         "погода",
#                         "forecast",
#                         "прогноз",
#                     ),
#                     LONDON_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Check the weather for tomorrow in Tokyo.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "weather",
#                         "погода",
#                         "forecast",
#                         "прогноз",
#                     ),
#                     TOKYO_CITY_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Check whether GitHub is currently available.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     (
#                         "GitHub",
#                         "гитхаб",
#                     ),
#                 ),
#             ),
#             ToolRouteTest(
#                 "Search for information about recursion.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Search for information about TCP.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Find Python documentation.",
#                 RouterTool.WEB_SEARCH,
#                 expected_query_requirements = (
#                     PYTHON_VARIANTS,
#                 ),
#             ),
#             ToolRouteTest(
#                 "Search for what pointers are in C++.",
#                 RouterTool.WEB_SEARCH,
#             ),
#             ToolRouteTest(
#                 "Find out how much the dollar costs right now.",
#                 RouterTool.WEB_SEARCH,
#             ),
#         ],
#     ),
# ]
