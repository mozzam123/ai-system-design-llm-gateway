from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import ChatService


def create_chat_router(chat_service: ChatService) -> APIRouter:
    router = APIRouter()

    @router.post("/chat", response_model=ChatResponse)
    async def chat(request: ChatRequest):
        return await chat_service.chat(request)

    return router
