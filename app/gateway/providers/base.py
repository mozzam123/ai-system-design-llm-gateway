from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    async def chat(
        self,
        model: str,
        messages: list[dict],
    ) -> str:
        pass
