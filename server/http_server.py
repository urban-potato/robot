import json
from http.server import BaseHTTPRequestHandler
from typing import Any

from ai.provider import AIProvider
from memory import ConversationMemory


class RobotServer(BaseHTTPRequestHandler):
    def __init__(
        self,
        ai_provider: AIProvider,
        memory: ConversationMemory,
        request: Any,
        client_address: Any,
        server: Any,
    ):
        self.ai_provider = ai_provider
        self.memory = memory
        super().__init__(request=request, client_address=client_address, server=server)

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
            answer = self.ai_provider.chat(self.memory)
            self.memory.add_assistant_message(answer)

        except Exception:
            self.send_error(500, "AI provider error")
            return

        # except Exception as error:
        #     print(f"AI provider error: {error}")
        #     raise

        response_body = json.dumps(
            {"answer": answer},
            ensure_ascii=False,
        ).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()

        self.wfile.write(response_body)