from collections.abc import Sequence

from ai.tool_classifier.types import ToolSelection
from tools.registry import Tool, TOOLS


class ToolSelector:
    def select(
        self,
        selection: ToolSelection,
    ) -> Sequence[Tool]:
        if selection.needs_web:
            return [TOOLS["web_search"]]

        return []