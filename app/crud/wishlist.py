from sqlmodel import Session

from app.models.wishlist import WishlistCreate, WishlistUpdate
from app.queries.wishlist import WishlistQuery


def create(session: Session, wishlist: WishlistCreate):
    query = WishlistQuery(session)

    query.create(wishlist)


def read(session: Session, wishlist_id: int):
    query = WishlistQuery(session)

    return query.query_id(wishlist_id)


def read_all(session: Session, skip: int = 0, limit: int = 100):
    query = WishlistQuery(session)

    return query.read_all(skip, limit)


def only_with_wishes(session: Session):
    query = WishlistQuery(session)

    return query.only_with_wishes()


def read_by_wishlist(session: Session, wishlist_id: int, skip: int = 0, limit: int = 100):
    query = WishlistQuery(session)

    return query.read_by_wishlist(skip, limit, wishlist_id)


def update(session: Session, wishlist_id: int, wishlist: WishlistUpdate):
    query = WishlistQuery(session)

    return query.update(wishlist_id, wishlist)


def delete(session: Session, wishlist_id: int):
    query = WishlistQuery(session)

    return query.delete(wishlist_id)
