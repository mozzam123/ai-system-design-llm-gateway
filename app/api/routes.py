from fastapi import APIRouter, HTTPException

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat import ChatService


def create_chat_router(chat_service: ChatService) -> APIRouter:
    router = APIRouter()

    @router.post("/chat", response_model=ChatResponse)
    async def chat(request: ChatRequest):
        try:
            return await chat_service.chat(request)

        except Exception as exc:
            raise HTTPException(
                status_code=502,
                detail=str(exc),
            )

    return router
