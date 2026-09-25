from config import (
    AI_PROVIDER,
    AIProviderType,
    OLLAMA_MODEL,
    OLLAMA_URL,
)

from .providers.ollama.ollama_ai_provider import OllamaAIProvider
from .ai_provider import AIProvider


def create_ai_provider() -> AIProvider:
    if AI_PROVIDER == AIProviderType.OLLAMA:
        return OllamaAIProvider(OLLAMA_URL, OLLAMA_MODEL)

    raise ValueError(f"Unknown AI provider: {AI_PROVIDER}")