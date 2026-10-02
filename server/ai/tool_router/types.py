from dataclasses import dataclass


@dataclass
class ToolRoute:
    tool: str | None
    arguments: dict[str, str]
    needs_clarification: bool
    clarification_question: str | None
    