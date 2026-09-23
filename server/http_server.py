import json
from http.server import BaseHTTPRequestHandler

from ai.provider import AIProvider


class RobotServer(BaseHTTPRequestHandler):
    def __init__(self, ai_provider: AIProvider, *args, **kwargs):
        self.ai_provider = ai_provider
        super().__init__(*args, **kwargs)

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
            answer = self.ai_provider.chat(user_message)

        except Exception:
            self.send_error(500, "AI provider error")
            return

        response_body = json.dumps(
            {"answer": answer},
            ensure_ascii=False,
        ).encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(response_body)))
        self.end_headers()

        self.wfile.write(response_body)