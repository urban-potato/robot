from dataclasses import dataclass


@dataclass(frozen=True)
class ToolSelection:
    needs_web: bool