from sqlmodel import select

from app.models.user import User
from app.queries.base import BaseQuery


class UserQuery(BaseQuery):
    def __init__(self, session, model=User):
        super().__init__(session, model)

    def query_username(self, username: str):
        statement = select(self.model).where(self.model.username == username)
        return self.query(statement).first()
