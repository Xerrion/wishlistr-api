from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.database import engine


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


# Instantiate the app
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="A wishlist API built with FastAPI, SQLModel, and SQLite.",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)
# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.add_event_handler("startup", create_db_and_tables)

app.include_router(api_router)
