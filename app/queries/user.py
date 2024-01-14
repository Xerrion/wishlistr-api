from app.models.user import User
from app.queries.base import BaseQuery


class UserQuery(BaseQuery):
    def __init__(self, session, model=User):
        super().__init__(session, model)

    def query_username(self, username: str):
        return self.query().filter(self.model.username == username).first()
