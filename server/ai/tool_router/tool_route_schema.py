from typing import Any

from .types import (
    RouterArgumentName,
    RouterField,
    RouterTool,
)


TOOL_ROUTE_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        RouterField.TOOL: {
            "type": "string",
            "enum": [
                tool.value
                for tool in RouterTool
            ],
        },
        RouterField.ARGUMENTS: {
            "type": "object",
            "properties": {
                RouterArgumentName.QUERY: {
                    "type": "string",
                },
                RouterArgumentName.URL: {
                    "type": "string",
                },
                RouterArgumentName.CITY: {
                    "type": "string",
                },
                RouterArgumentName.COUNTRY_CODE: {
                    "type": "string",
                },
                RouterArgumentName.TIMEZONE: {
                    "type": "string",
                },
                RouterArgumentName.QUESTION: {
                    "type": "string",
                },
            },
            "additionalProperties": False,
        },
    },
    "required": [
        RouterField.TOOL,
    ],
    "additionalProperties": False,
}
