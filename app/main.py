from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers import wish_router, user_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Instantiate the app
app = FastAPI()

# Include routers
app.include_router(wish_router.router)
app.include_router(user_router.router)
