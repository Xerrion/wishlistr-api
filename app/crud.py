from sqlalchemy.orm import Session

from app import auth, schemas, models
from app.models import wish, user
from app.models.user import User


def create_wish(db: Session, wish: schemas.wish.WishCreate):
    db_wish = models.wish.Wish(**wish.model_dump())
    db.add(db_wish)
    db.commit()
    db.refresh(db_wish)
    return db_wish


def get_wish(db: Session, wish_id: int):
    return db.query(models.wish.Wish).filter(models.wish.Wish.id == wish_id).first()


def get_wishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.wish.Wish).offset(skip).limit(limit).all()


def update_wish(db: Session, wish_id: int, wish: schemas.wish.WishUpdate):
    db_wish = db.query(models.wish.Wish).filter(models.wish.Wish.id == wish_id).first()
    if db_wish:
        update_data = wish.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_wish, key, value)
        db.commit()
        db.refresh(db_wish)
    return db_wish


def delete_wish(db: Session, wish_id: int):
    db_wish = db.query(models.wish.Wish).filter(models.wish.Wish.id == wish_id).first()
    if db_wish:
        db.delete(db_wish)
        db.commit()
        return True
    return False


def create_user(db: Session, user: schemas.user.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.user.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str):
    return db.query(models.user.User).filter(models.user.User.username == username).first()


def create_initial_user(db: Session, username: str, password: str):
    user = db.query(models.user.User).filter(models.user.User.username == username).first()
    if not user:
        hashed_password = auth.get_password_hash(password)
        db_user = User(username=username, hashed_password=hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
