from fastapi import FastAPI
from sqlmodel import SQLModel
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import api_router
from app.core.config import settings
from app.database import engine


def init_db():
    # Create the initial data
    from app.crud import wishlist as wishlist_crud
    from app.crud import wish as wish_crud
    from app.models.wishlist import WishlistCreate
    from app.models.wish import WishCreate
    from app.crud import user as user_crud
    from app.database import get_session
    from app.models.user import UserCreate, Role
    from app.models.wishlist import Wishlist

    session = next(get_session())

    if session.get(Wishlist, 1):
        return

    wishlist = WishlistCreate(title="My Wishlist", description="My wishlist description")
    wishlist_crud.create(session, wishlist=wishlist)

    wish = WishCreate(
        title="My wish",
        description="My wish description",
        url="https://example.com",
        image_url="https://example.com/image.jpg",
        wishlist_id=1,
    )
    wish_crud.create(session, wish=wish)

    user = UserCreate(username="admin", password="admin", role=Role.ADMIN)
    user_crud.create(user=user, session=session)


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
app.add_event_handler("startup", init_db)

app.include_router(api_router)
