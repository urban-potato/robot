from dataclasses import dataclass
from typing import Any, Callable

from .time import get_current_time


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict[str, Any]
    function: Callable[..., str]


TIME_TOOL = Tool(
    name="get_current_time",
    description="Get the current date and time.",
    parameters={
        "type": "object",
        "properties": {},
        "required": [],
    },
    function=get_current_time,
)

TOOLS = {
    TIME_TOOL.name: TIME_TOOL,
}
