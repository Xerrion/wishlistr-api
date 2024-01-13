from pydantic import BaseModel


class WishBase(BaseModel):
    title: str
    description: str
    url: str  # URL of the wish
    image_url: str  # URL of the wish's image


class WishCreate(WishBase):
    pass


class WishUpdate(WishBase):
    pass


class Wish(WishBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
