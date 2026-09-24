from .time import get_current_time


def execute_tool(name: str, arguments: dict) -> str:
    if name == "get_current_time":
        return get_current_time()

    raise ValueError(f"Unknown tool: {name}")