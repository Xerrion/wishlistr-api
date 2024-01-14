from sqlmodel import create_engine, Session

from app.core.config import settings

sqlite_file_name = ""

connect_args = {"check_same_thread": False}
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, echo=True, connect_args=connect_args)


def get_session():
    with Session(engine) as session:
        yield session
