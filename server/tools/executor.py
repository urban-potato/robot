from typing import Any

from .registry import TOOLS


def execute_tool(name: str, arguments: dict[str, Any]) -> str:
    if name not in TOOLS:
        raise ValueError(f"Unknown tool: {name}")

    tool = TOOLS[name]

    return tool.function(**arguments)