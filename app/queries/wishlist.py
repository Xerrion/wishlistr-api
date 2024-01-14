from app.models.wishlist import Wishlist
from app.queries.base import BaseQuery


class WishlistQuery(BaseQuery):
    def __init__(self, session):
        super().__init__(session, Wishlist)

    def read_by_wishlist(self, skip: int = 0, limit: int = 100, wishlist_id: int = None):
        return self.query().filter(self.model.wishlist_id == wishlist_id).offset(skip).limit(limit).all()
