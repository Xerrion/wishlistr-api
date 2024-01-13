# app/schemas/wish.py
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
        from_attributes = True
