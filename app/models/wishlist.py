from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field, Relationship

from app.models.wish import Wish


class WishlistBase(SQLModel):
    title: str
    description: Optional[str] = None


class Wishlist(WishlistBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    wishes: List[Wish] = Relationship(back_populates="wishlist")
    is_public: bool = True
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
    updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)


class WishlistCreate(WishlistBase):
    is_public: Optional[bool] = True


class WishlistRead(WishlistBase):
    wishes: List[Wish]


class WishlistUpdate(WishlistBase):
    is_public: Optional[bool] = None
    updated_at: datetime = datetime.utcnow()


class WishlistDelete(WishlistBase):
    pass
