# app/models/wishes.py
from datetime import datetime
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
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    is_public: bool = True
    is_reserved: bool = False


class WishCreate(WishBase):
    wishlist_id: int


class WishRead(WishBase):
    wishlist_id: int
    wishlist: "Wishlist"


class WishUpdate(WishBase):
    wishlist_id: Optional[int] = None
    is_public: Optional[bool] = None
    is_reserved: Optional[bool] = None
    updated_at: datetime = datetime.utcnow()


class WishDelete(WishBase):
    pass
