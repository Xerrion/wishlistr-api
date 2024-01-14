from app.models.wish import Wish
from app.queries.base import BaseQuery


class WishQuery(BaseQuery):
    def __init__(self, session):
        super().__init__(session, Wish)

    def query_wishes_by_wishlist(self, wishlist_id: int):
        return self.query().filter(self.model.wishlist_id == wishlist_id)
