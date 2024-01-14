from enum import Enum
from typing import Optional

from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


class UserBase(SQLModel):
    username: str
    role: Role = Role.USER


class User(UserBase, table=True):
    id: int | None = Field(default=None, primary_key=True, index=True)
    hashed_password: str


class UserCreate(SQLModel):
    username: str
    password: str


class UserRead(UserBase):
    id: int


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
