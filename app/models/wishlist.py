from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from app.models.wish import Wish


class WishlistBase(SQLModel):
    title: str
    description: str | None = None


class Wishlist(WishlistBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    wishes: List["Wish"] = Relationship(back_populates="wishlist")


class WishlistCreate(WishlistBase):
    title: str
    description: str | None = None


class WishlistRead(WishlistBase):
    title: str
    description: str
    wishes: List["Wish"]


class WishlistUpdate(WishlistBase):
    pass


class WishlistDelete(WishlistBase):
    pass
