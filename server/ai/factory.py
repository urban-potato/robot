from .config import (
    AI_PROVIDER,
    AIProviderType,
    OLLAMA_MODEL,
    OLLAMA_URL,
)

from .ollama import OllamaProvider
from .provider import AIProvider


def create_ai_provider() -> AIProvider:
    if AI_PROVIDER == AIProviderType.OLLAMA:
        return OllamaProvider(OLLAMA_URL, OLLAMA_MODEL)

    raise ValueError(f"Unknown AI provider: {AI_PROVIDER}")