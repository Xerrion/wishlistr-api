from sqlmodel import Session, select


class BaseQuery:
    def __init__(self, session: Session, model=None):
        self.session: Session = session
        self.model = model

    def query(self, statement):
        return self.session.exec(statement)

    def query_id(self, _id: int):
        statement = select(self.model).where(self.model.id == _id)
        return self.query(statement)

    def create(self, schema):
        row = self.model(**schema.model_dump())
        self.session.add(row)
        self.session.commit()
        self.session.refresh(row)
        return row

    def read_all(self, skip: int = 0, limit: int = 100):
        statement = select(self.model).offset(skip).limit(limit)
        return self.query(statement=statement).all()

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
