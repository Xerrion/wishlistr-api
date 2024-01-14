from app.api.deps import SessionDep
from app.models.wish import WishUpdate, WishCreate
from app.queries.wish import WishQuery


def create(session: SessionDep, wish: WishCreate):
    query = WishQuery(session)

    return query.create(wish)


def read(session: SessionDep, wish_id: int):
    query = WishQuery(session)

    return query.query_id(wish_id).first()


def read_all(session: SessionDep, skip: int = 0, limit: int = 100):
    query = WishQuery(session)

    return query.read_all(skip, limit)


def update(session: SessionDep, wish_id: int, wish: WishUpdate):
    query = WishQuery(session)

    return query.update(wish_id, wish)


def delete(session: SessionDep, wish_id: int):
    query = WishQuery(session)

    query.delete(wish_id)
