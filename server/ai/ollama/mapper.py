from typing import Any

from tools.registry import Tool


def to_ollama_tool(tool: Tool) -> dict[str, Any]:
    return {
        "type": "function",
        "function": {
            "name": tool.name,
            "description": tool.description,
            "parameters": tool.parameters,
        },
    }


def get_ollama_tools(tools: list[Tool]) -> list[dict[str, Any]]:
    return [
        to_ollama_tool(tool)
        for tool in tools
    ]
