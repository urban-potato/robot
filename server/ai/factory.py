from config import (
    AI_PROVIDER,
    AIProviderType,
    OLLAMA_MODEL,
    OLLAMA_URL,
)

from .providers.ollama.ollama_provider import OllamaProvider
from .ai_provider import AIProvider


def create_ai_provider() -> AIProvider:
    if AI_PROVIDER == AIProviderType.OLLAMA:
        return OllamaProvider(OLLAMA_URL, OLLAMA_MODEL)

    raise ValueError(f"Unknown AI provider: {AI_PROVIDER}")