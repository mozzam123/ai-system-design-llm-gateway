from app.gateway.providers.base import LLMProvider


class ModelRouter:

    def __init__(self, providers: dict[str, LLMProvider]):
        self.providers = providers

    def route(self, model: str) -> LLMProvider:
        provider = self.providers.get("ollama")

        if not provider:
            raise ValueError("No provider available for Ollama")

        return provider
