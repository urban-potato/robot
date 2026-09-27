from functools import partial
from http.server import HTTPServer

from ai.factory import create_ai_provider
from http_server import RobotServer
from assistant.system_prompt import build_system_prompt
from conversation_memory.conversation_memory import ConversationMemory
from ai.tool_classifier.tool_classifier import ToolClassifier
from ai.tool_selection.tool_selector import ToolSelector
from config import OLLAMA_URL, TOOL_CLASSIFIER_MODEL


ai_provider = create_ai_provider()
system_prompt = build_system_prompt()
memory = ConversationMemory(system_prompt)
tool_classifier = ToolClassifier(
    ollama_url=OLLAMA_URL,
    model=TOOL_CLASSIFIER_MODEL,
)
tool_selector = ToolSelector()

handler = partial(
    RobotServer,
    ai_provider,
    memory,
    tool_classifier,
    tool_selector,
)

server = HTTPServer(("localhost", 8000), handler)

print("Robot server is running on http://localhost:8000")

server.serve_forever()