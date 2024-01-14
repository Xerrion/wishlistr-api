from sqlalchemy.orm import Session

from app.core import security
from app.models.user import User, UserCreate, UserUpdate
from app.queries.user import UserQuery


def create(*, session: Session, user: UserCreate) -> User:
    query = UserQuery(session=session)
    db_user = User()
    db_user.username = user.username
    db_user.hashed_password = security.get_password_hash(user.password)
    new_user = User.model_validate(db_user)

    return query.create(new_user)


def read(*, session: Session, user_id: int) -> User:
    query = UserQuery(session=session)
    db_user = query.query_id(user_id)

    return db_user


def read_by_username(*, session: Session, username: str) -> User:
    query = UserQuery(session=session)
    db_user = query.query_username(username=username)

    return db_user


def update(*, session: Session, user_id, user: UserUpdate) -> User:
    query = UserQuery(session=session)
    db_user = query.update(user_id, schema=user)

    return db_user


def delete(*, session: Session, user_id: int) -> User:
    query = UserQuery(session=session)
    db_user = query.delete(user_id)

    return db_user
