from dataclasses import dataclass
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


def _empty_arguments() -> dict[str, str]:
    return {}


@dataclass
class ToolRoute:
    tool: RouterTool
    # arguments: dict[str, str] | None = None
    arguments: dict[str, str] = field(default_factory=_empty_arguments)

class RouterArgumentNormalization(str, Enum):
    NONE = "none"
    UPPERCASE = "uppercase"

class RouterField:
    TOOL = "tool"
    ARGUMENTS = "arguments"

class RouterArgumentName:
    QUERY = "query"
    URL = "url"
    CITY = "city"
    COUNTRY_CODE = "country_code"
    TIMEZONE = "timezone"
    QUESTION = "question"


class RouterTool(str, Enum):
    WEB_SEARCH = "web_search"
    WEB_PAGE_READ = "web_page_read"
    GET_DATETIME = "get_datetime"
    DEFAULT_ASSISTANT = "default_assistant"
    CLARIFICATION = "clarification"

    @property
    def arguments(self) -> list[RouterArgument]:
        match self:
            case RouterTool.WEB_SEARCH:
                return [
                    RouterArgument(
                        RouterArgumentName.QUERY,
                        True,
                    ),
                ]

            case RouterTool.WEB_PAGE_READ:
                return [
                    RouterArgument(
                        RouterArgumentName.URL,
                        True,
                    ),
                ]

            case RouterTool.GET_DATETIME:
                return [
                    RouterArgument(RouterArgumentName.CITY),
                    RouterArgument(
                        RouterArgumentName.COUNTRY_CODE,
                        normalization=RouterArgumentNormalization.UPPERCASE,
                    ),
                    RouterArgument(RouterArgumentName.TIMEZONE),
                ]

            case RouterTool.DEFAULT_ASSISTANT:
                return []

            case RouterTool.CLARIFICATION:
                return [
                    RouterArgument(
                        RouterArgumentName.QUESTION,
                        True,
                    ),
                ]

    def normalize_arguments(
        self,
        arguments: dict[str, Any],
    ) -> dict[str, str]:
        normalized: dict[str, str] = {}

        for argument in self.arguments:
            value = argument.normalize(arguments)

            if value is not None:
                normalized[argument.name] = value

        return normalized

    @property
    def required_arguments(self) -> list[str]:
        return [
            argument.name
            for argument in self.arguments
            if argument.required
        ]

    @property
    def optional_arguments(self) -> list[str]:
        return [
            argument.name
            for argument in self.arguments
            if not argument.required
        ]

@dataclass(frozen=True)
class RouterArgument:
    name: str
    required: bool = False
    normalization: RouterArgumentNormalization = RouterArgumentNormalization.NONE

    def normalize(
        self,
        arguments: dict[str, Any],
    ) -> str | None:
        value = arguments.get(self.name)

        if not isinstance(value, str):
            value = None
        else:
            value = value.strip()

            if not value:
                value = None

        if value is None:
            if self.required:
                raise ValueError(
                    f"Required router argument is missing: {self.name!r}."
                )

            return None

        match self.normalization:
            case RouterArgumentNormalization.NONE:
                pass

            case RouterArgumentNormalization.UPPERCASE:
                value = value.upper()

        return value
    