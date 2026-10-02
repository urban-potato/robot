from functools import partial
from http.server import HTTPServer

from ai.factory import create_ai_provider
from ai.tool_router.semantic_tool_router import SemanticToolRouter
from assistant.system_prompt import build_system_prompt
from config import TOOL_CLASSIFIER_MODEL, OLLAMA_URL
from conversation_memory.conversation_memory import ConversationMemory
from http_server import RobotServer


ai_provider = create_ai_provider()
system_prompt = build_system_prompt()
memory = ConversationMemory(system_prompt)

tool_router = SemanticToolRouter(
    ollama_url=OLLAMA_URL,
    model=TOOL_CLASSIFIER_MODEL,
)

handler = partial(
    RobotServer,
    ai_provider,
    memory,
    tool_router,
)

server = HTTPServer(("localhost", 8000), handler)

print("Robot server is running on http://localhost:8000")

server.serve_forever()
