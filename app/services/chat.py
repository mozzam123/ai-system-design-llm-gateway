from app.gateway.router import ModelRouter
from app.schemas.chat import ChatRequest, ChatResponse


class ChatService:

    def __init__(self, router: ModelRouter):
        self.router = router

    async def chat(self, request: ChatRequest) -> ChatResponse:
        provider = self.router.route(request.model)

        messages = [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in request.messages
        ]

        response = await provider.chat(
            model=request.model,
            messages=messages,
        )

        return ChatResponse(
            model=request.model,
            provider="ollama",
            response=response,
        )
