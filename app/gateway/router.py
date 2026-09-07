from app.gateway.providers.base import LLMProvider


class ModelRouter:

    def __init__(self, model_providers: dict[str, LLMProvider]):
        self.model_providers = model_providers

    def route(self, model: str) -> LLMProvider:
        provider = self.model_providers.get(model)

        if not provider:
            raise ValueError(f"No provider configured for model: {model}")

        return provider
