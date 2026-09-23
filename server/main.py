from functools import partial
from http.server import HTTPServer

from ai.factory import create_ai_provider
from http_server import RobotServer
from memory import ConversationMemory


ai_provider = create_ai_provider()
memory = ConversationMemory()

handler = partial(RobotServer, ai_provider, memory)

server = HTTPServer(("localhost", 8000), handler)

print("Robot server is running on http://localhost:8000")

server.serve_forever()