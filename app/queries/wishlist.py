from sqlmodel import select

from app.models.wishlist import Wishlist
from app.queries.base import BaseQuery


class WishlistQuery(BaseQuery):
    def __init__(self, session):
        super().__init__(session, Wishlist)

    def read_all(self, skip: int = 0, limit: int = 100):
        statement = select(self.model).offset(skip).limit(limit).where(self.model.is_public == True)
        return self.query(statement)

    def read_by_wishlist(self, skip: int = 0, limit: int = 100, wishlist_id: int = None):
        statement = select(self.model).where(self.model.id == wishlist_id).offset(skip).limit(limit)
        return self.query(statement).all()

    def only_with_wishes(self):
        statement = select(self.model).where(self.model.wishes != None).where(self.model.is_public == True)
        return self.query(statement).all()
