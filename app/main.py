from fastapi import FastAPI
from dotenv import load_dotenv

from app.api.routes import create_chat_router
from app.gateway.providers.groq import GroqProvider
from app.gateway.providers.ollama import OllamaProvider
from app.gateway.router import ModelRouter
from app.services.chat import ChatService

load_dotenv()


def create_app() -> FastAPI:
    app = FastAPI(title="AI Gateway")

    ollama_provider = OllamaProvider()
    groq_provider = GroqProvider()

    model_router = ModelRouter(
        model_providers={
            "qwen3:8b": ollama_provider,
            "openai/gpt-oss-20b": groq_provider,
        }
    )

    chat_service = ChatService(
        router=model_router,
    )

    app.include_router(create_chat_router(chat_service))

    return app


app = create_app()
