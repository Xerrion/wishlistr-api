from sqlmodel import select

from app.models.wish import Wish
from app.queries.base import BaseQuery


class WishQuery(BaseQuery):
    def __init__(self, session):
        super().__init__(session, Wish)

    def query_wishes_by_wishlist(self, wishlist_id: int):
        statement = select(self.model).where(self.model.wishlist_id == wishlist_id)
        return self.query(statement)
