from dataclasses import dataclass
from typing import Any


@dataclass
class ToolRoute:
    tool: str | None
    arguments: dict[str, Any]
    