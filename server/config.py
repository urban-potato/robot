import os
from enum import Enum

from dotenv import load_dotenv


class AIProviderType(Enum):
    OLLAMA = "ollama"


load_dotenv()


AI_PROVIDER = AIProviderType(
    os.environ["AI_PROVIDER"],
)

OLLAMA_URL = os.environ["OLLAMA_URL"]
OLLAMA_MODEL = os.environ["OLLAMA_MODEL"]

SEARXNG_URL = os.environ["SEARXNG_URL"]