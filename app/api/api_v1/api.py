from fastapi import APIRouter

from app.api.api_v1.endpoints import login, users, wishlists, wishes

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(wishlists.router, prefix="/wishlists", tags=["wishlists"])
api_router.include_router(wishes.router, prefix="/wishes", tags=["wishes"])
