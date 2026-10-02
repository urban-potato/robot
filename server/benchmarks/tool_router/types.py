from typing import Any, TypedDict


class OllamaTiming(TypedDict):
    ollama_total: float | None
    load: float | None
    prompt_eval: float | None
    eval: float | None


class ResultRow(TypedDict):
    test: int
    group: str
    message: str
    wall_time: float
    ollama_total: float | None
    load: float | None
    prompt_eval: float | None
    eval: float | None
    tool: str | None
    arguments: dict[str, Any] | None
    needs_clarification: bool | None
    clarification_question: str | None
    route_correct: bool
    validation_errors: str
    error: str
    