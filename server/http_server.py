import json
from http.server import BaseHTTPRequestHandler
import time
from typing import Any
from uuid import uuid4

from ai.ai_provider import AIProvider
from ai.tool_router.semantic_tool_router import SemanticToolRouter
from conversation_memory.conversation_memory import ConversationMemory
from tools.executor import ToolExecutionError, execute_tool


class RobotServer(BaseHTTPRequestHandler):
    def __init__(
        self,
        ai_provider: AIProvider,
        memory: ConversationMemory,
        tool_router: SemanticToolRouter,
        request: Any,
        client_address: Any,
        server: Any,
    ):
        self.ai_provider = ai_provider
        self.memory = memory
        self.tool_router = tool_router
        super().__init__(
            request=request,
            client_address=client_address,
            server=server,
        )

    def do_POST(self):
        if self.path != "/chat":
            self.send_error(404)
            return

        try:
            content_length = int(self.headers["Content-Length"])
            body = self.rfile.read(content_length)
            request_data = json.loads(body)
            user_message = request_data["message"]
        except (json.JSONDecodeError, KeyError):
            self.send_error(400, "Invalid request")
            return

        try:
            self.memory.add_user_message(user_message)

            router_start = time.perf_counter()
            route = self.tool_router.route(user_message)
            router_elapsed = time.perf_counter() - router_start

            print(
                f"Tool router: {router_elapsed:.3f} s "
                f"({route})"
            )

            if route.needs_clarification:
                answer = route.clarification_question

                if answer is None:
                    raise ValueError(
                        "Router requested clarification "
                        "without a clarification question."
                    )
            else:
                if route.tool is not None:
                    tool_call_id = str(uuid4())

                    self.memory.add_tool_call(
                        tool_call_id=tool_call_id,
                        tool_name=route.tool,
                        arguments=route.arguments,
                    )

                    try:
                        tool_result = execute_tool(
                            route.tool,
                            route.arguments,
                        )
                    except ToolExecutionError as error:
                        tool_result = str(error)

                    self.memory.add_tool_message(
                        tool_call_id=tool_call_id,
                        tool_name=route.tool,
                        content=tool_result,
                    )

                answer = self.ai_provider.chat(
                    self.memory,
                    tools=None,
                )

            self.memory.add_assistant_message(answer)

        except Exception:
            self.send_error(500, "AI provider error")
            return

        response_body = json.dumps(
            {"answer": answer},
            ensure_ascii=False,
        ).encode("utf-8")

        self.send_response(200)
        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8",
        )
        self.send_header(
            "Content-Length",
            str(len(response_body)),
        )
        self.end_headers()
        self.wfile.write(response_body)
