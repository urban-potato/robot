from functools import partial
from http.server import HTTPServer

from ai.factory import create_ai_provider
from http_server import RobotServer
from assistant.system_prompt import build_system_prompt
from conversation_memory.conversation_memory import ConversationMemory


ai_provider = create_ai_provider()
system_prompt = build_system_prompt()
memory = ConversationMemory(system_prompt)

handler = partial(RobotServer, ai_provider, memory)

server = HTTPServer(("localhost", 8000), handler)

print("Robot server is running on http://localhost:8000")

server.serve_forever()