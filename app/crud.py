from sqlalchemy.orm import Session

from app import models, schemas, auth


def create_wish(db: Session, wish: schemas.WishCreate):
    db_wish = models.Wish(**wish.model_dump())
    db.add(db_wish)
    db.commit()
    db.refresh(db_wish)
    return db_wish


def get_wish(db: Session, wish_id: int):
    return db.query(models.Wish).filter(models.Wish.id == wish_id).first()


def get_wishes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Wish).offset(skip).limit(limit).all()


def update_wish(db: Session, wish_id: int, wish: schemas.WishUpdate):
    db_wish = db.query(models.Wish).filter(models.Wish.id == wish_id).first()
    if db_wish:
        update_data = wish.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_wish, key, value)
        db.commit()
        db.refresh(db_wish)
    return db_wish


def delete_wish(db: Session, wish_id: int):
    db_wish = db.query(models.Wish).filter(models.Wish.id == wish_id).first()
    if db_wish:
        db.delete(db_wish)
        db.commit()
        return True
    return False


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
