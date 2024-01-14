from sqlalchemy.orm import Session


class BaseQuery:
    def __init__(self, session: Session, model=None):
        self.session = session
        self.model = model

    def query(self):
        return self.session.query(self.model)

    def query_id(self, _id: int):
        return self.session.get(self.model, _id)

    def create(self, schema):
        row = self.model(**schema.model_dump())
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def read_all(self, skip: int = 0, limit: int = 100):
        return self.query().offset(skip).limit(limit).all()

    def delete(self, _id: int):
        row = self.query_id(_id)
        if row:
            self.session.delete(row)
            self.session.commit()
            return True
        return False

    def update(self, _id, schema):
        row = self.query_id(_id)
        if row:
            update_data = schema.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(row, key, value)
            self.session.commit()
            self.session.refresh(row)
        return row
