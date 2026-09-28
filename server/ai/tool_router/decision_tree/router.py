from typing import Any

from .types import ToolRoute

from .nodes import (
    DecisionTreeLLM,
    extract_url,
)

from .prompts import (
    BINARY_SYSTEM_PROMPT,
    CURRENT_TIME_PROMPT,
    PAGE_READ_PROMPT,
    WEB_SEARCH_PROMPT,
    CLARIFICATION_PROMPT,
    SEARCH_QUERY_PROMPT,
)


class DecisionTreeRouter:
    """
    Tool router based on a sequence of small decisions.

    Unlike SemanticToolRouter, the model is not asked to choose
    between all tools at once.

    Instead, the request passes through a decision tree.
    """

    def __init__(
        self,
        ollama_url: str,
        model: str,
    ):
        self.ollama_url = ollama_url
        self.model = model
        self.llm = DecisionTreeLLM(
            ollama_url=ollama_url,
            model=model,
        )

    def route(self, message: str) -> ToolRoute:
        """
        Route one user message through the decision tree.
        """

        # ---------------------------------------------------------
        # NODE 1
        # Does the user need the actual current date/time?
        # ---------------------------------------------------------

        if self._needs_current_time(message):
            return ToolRoute(
                tool="get_current_time",
                arguments={},
                needs_clarification=False,
                clarification_question=None,
            )

        # ---------------------------------------------------------
        # NODE 2
        # Is there an explicit URL?
        # ---------------------------------------------------------

        url = extract_url(message)

        if url is not None:

            # -----------------------------------------------------
            # NODE 2A
            # Does the user want the contents of this URL?
            # -----------------------------------------------------

            if self._needs_page_read(message):
                return ToolRoute(
                    tool="web_page_read",
                    arguments={
                        "url": url,
                    },
                    needs_clarification=False,
                    clarification_question=None,
                )

        # ---------------------------------------------------------
        # NODE 3
        # Does the request require internet information?
        # ---------------------------------------------------------

        if self._needs_web_search(message):

            # -----------------------------------------------------
            # NODE 3A
            # Before searching, check whether an essential target
            # is missing.
            # -----------------------------------------------------

            if self._needs_clarification(message):
                return ToolRoute(
                    tool=None,
                    arguments={},
                    needs_clarification=True,
                    clarification_question=self._generate_clarification(
                        message
                    ),
                )

            # -----------------------------------------------------
            # NODE 3B
            # The tool is known.
            # -----------------------------------------------------

            query = self._generate_search_query(message)

            return ToolRoute(
                tool="web_search",
                arguments={
                    "query": query,
                },
                needs_clarification=False,
                clarification_question=None,
            )

        # ---------------------------------------------------------
        # NODE 4
        #
        # No current time.
        # No page reading.
        # No web search.
        #
        # Could this still require clarification?
        # ---------------------------------------------------------

        if self._needs_clarification(message):
            return ToolRoute(
                tool=None,
                arguments={},
                needs_clarification=True,
                clarification_question=self._generate_clarification(
                    message
                ),
            )

        # ---------------------------------------------------------
        # NODE 5
        #
        # Stable knowledge / ordinary conversation.
        # ---------------------------------------------------------

        return ToolRoute(
            tool=None,
            arguments={},
            needs_clarification=False,
            clarification_question=None,
        )

    # =============================================================
    # Decision nodes
    # =============================================================

    def _needs_current_time(self, message: str) -> bool:
        """
        NODE 1:
        Does the user need the actual current date/time?
        """

        return self.llm.classify_binary(
            system_prompt=(
                BINARY_SYSTEM_PROMPT
                + "\n"
                + CURRENT_TIME_PROMPT
            ),
            message=message,
        )

    def _needs_page_read(self, message: str) -> bool:
        """
        NODE 2A:
        Does the user want to inspect the contents of the URL?
        """

        return self.llm.classify_binary(
            system_prompt=(
                BINARY_SYSTEM_PROMPT
                + "\n"
                + PAGE_READ_PROMPT
            ),
            message=message,
        )

    def _needs_web_search(self, message: str) -> bool:
        """
        NODE 3:
        Does the request require internet information?
        """

        return self.llm.classify_binary(
            system_prompt=(
                BINARY_SYSTEM_PROMPT
                + "\n"
                + WEB_SEARCH_PROMPT
            ),
            message=message,
        )

    def _needs_clarification(self, message: str) -> bool:
        """
        NODE 3A / NODE 4:
        Is essential information missing for the requested
        external action?
        """

        return self.llm.classify_binary(
            system_prompt=(
                BINARY_SYSTEM_PROMPT
                + "\n"
                + CLARIFICATION_PROMPT
            ),
            message=message,
        )

    # =============================================================
    # Generation nodes
    # =============================================================

    def _generate_search_query(self, message: str) -> str:
        """
        Generate the actual search-engine query.

        This happens ONLY after the tree has already selected
        web_search.
        """

        return self.llm.generate_search_query(
            system_prompt=SEARCH_QUERY_PROMPT,
            message=message,
        )

    def _generate_clarification(self, message: str) -> str:
        """
        Generate a clarification question in the user's language.

        This is intentionally a separate generation step from
        deciding whether clarification is necessary.
        """

        prompt = """
Generate one concise clarification question for the user's request.

The question must ask only for the missing essential information.

Write the question in the same language as the user's message.

Return ONLY valid JSON:
{"question": "..."}
"""

        request_data: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {
                    "role": "system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
            "stream": False,
            "format": {
                "type": "object",
                "properties": {
                    "question": {
                        "type": "string",
                    },
                },
                "required": ["question"],
                "additionalProperties": False,
            },
            "options": {
                "temperature": 0,
            },
        }

        result = self.llm.request(request_data)

        return result["question"]
    