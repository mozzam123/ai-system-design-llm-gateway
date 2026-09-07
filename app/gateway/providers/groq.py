import os

import httpx

from app.gateway.providers.base import LLMProvider


class GroqProvider(LLMProvider):

    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1"

    async def chat(
        self,
        model: str,
        messages: list[dict],
    ) -> str:

        if not self.api_key:
            raise RuntimeError("GROQ_API_KEY is not configured")

        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": model,
                    "messages": messages,
                },
            )

            if response.status_code != 200:
                print(response.text)

            response.raise_for_status()

            data = response.json()

            return data["choices"][0]["message"]["content"]
