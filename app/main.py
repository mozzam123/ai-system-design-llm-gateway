from fastapi import FastAPI

from app.api.routes import create_chat_router
from app.gateway.router import ModelRouter
from app.gateway.providers.ollama import OllamaProvider
from app.services.chat import ChatService


def create_app() -> FastAPI:
    app = FastAPI(title="AI Gateway")

    ollama_provider = OllamaProvider()

    model_router = ModelRouter(
        providers={
            "ollama": ollama_provider,
        }
    )

    chat_service = ChatService(
        router=model_router,
    )

    app.include_router(create_chat_router(chat_service))

    return app


app = create_app()
