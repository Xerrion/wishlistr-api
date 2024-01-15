from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


class UserBase(SQLModel):
    username: str


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    hashed_password: str
    role: Role = Role.USER
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class UserCreate(UserBase):
    username: str
    password: str
    role: Optional[Role] = Role.USER


class UserRead(UserBase):
    id: int
    username: str
    created_at: datetime


class UserUpdate(UserBase):
    username: str | None = None
    password: str | None = None


class UserDelete(UserBase):
    pass


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenPayload(BaseModel):
    username: str | None = None
