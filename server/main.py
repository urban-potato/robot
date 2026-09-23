from functools import partial
from http.server import HTTPServer

from ai.factory import create_ai_provider
from http_server import RobotServer


ai_provider = create_ai_provider()

handler = partial(RobotServer, ai_provider)

server = HTTPServer(("localhost", 8000), handler)

print("Robot server is running on http://localhost:8000")

server.serve_forever()