# app/models/wishes.py
from typing import Optional

from sqlmodel import SQLModel, Field, Relationship


class WishBase(SQLModel):
    title: str
    description: str
    url: str  # URL of the wish
    image_url: str  # URL of the wish's image


class Wish(WishBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    wishlist_id: int = Field(default=None, foreign_key="wishlist.id")  # ID of the wishlist the wish belongs to
    wishlist: "Wishlist" = Relationship(back_populates="wishes")


class WishCreate(WishBase):
    wishlist_id: int


class WishRead(WishBase):
    pass


class WishUpdate(WishBase):
    pass


class WishDelete(WishBase):
    pass
