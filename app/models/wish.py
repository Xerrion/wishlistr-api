# app/models/wish.py
from sqlalchemy import Column, Integer, String

from app.models import Base


class Wish(Base):
    __tablename__ = "wishes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    url = Column(String, index=True)  # URL of the wish
    image_url = Column(String, index=True)  # URL of the wish's image
