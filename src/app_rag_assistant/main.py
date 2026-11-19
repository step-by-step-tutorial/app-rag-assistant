from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app_rag_assistant.api.health import router as health_router
from app_rag_assistant.config import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    # startup: later we open the DB pool and LLM client here
    yield
    # shutdown: and close them here


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, lifespan=lifespan)
    app.include_router(health_router)
    return app


app = create_app()
