from fastapi import FastAPI

from app import models, routers, crud
from app.database import engine, SessionLocal

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Instantiate the app
app = FastAPI()


def create_start_user():
    db = SessionLocal()
    try:
        crud.create_initial_user(db=db, username="admin", password="admin123")
    finally:
        db.close()


app.add_event_handler("startup", create_start_user)

# Include routers
app.include_router(routers.wish.router)
app.include_router(routers.user.router)
