from sqlmodel import Session

from app.models.wish import WishUpdate, WishCreate
from app.queries.wish import WishQuery


def create(session: Session, wish: WishCreate):
    query = WishQuery(session)

    return query.create(wish)


def read(session: Session, wish_id: int):
    query = WishQuery(session)

    return query.query_id(wish_id).first()


def read_all(session: Session, skip: int = 0, limit: int = 100):
    query = WishQuery(session)

    return query.read_all(skip, limit)


def update(session: Session, wish_id: int, wish: WishUpdate):
    query = WishQuery(session)

    return query.update(wish_id, wish)


def delete(session: Session, wish_id: int):
    query = WishQuery(session)

    return query.delete(wish_id)
