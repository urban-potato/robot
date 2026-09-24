from typing import Any

from .registry import TOOLS


class ToolExecutionError(Exception):
    pass


def execute_tool(name: str, arguments: dict[str, Any]) -> str:
    if name not in TOOLS:
        raise ToolExecutionError(
            f"Unknown tool: {name}"
        )

    tool = TOOLS[name]

    try:
        return tool.function(**arguments)
    except Exception as error:
        raise ToolExecutionError(
            f"Tool '{name}' failed: {error}"
        ) from error