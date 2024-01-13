from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, schemas, auth, database

router = APIRouter(prefix="/wishes", tags=["wishes"])


@router.get("/", response_model=List[schemas.Wish])
def read_wishes(
    skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)
):
    return crud.get_wishes(db, skip, limit)


@router.get("/{wish_id}", response_model=schemas.Wish)
def read_wish(wish_id: int, db: Session = Depends(database.get_db)):
    wish = crud.get_wish(db, wish_id)
    if wish is None:
        raise HTTPException(status_code=404, detail="Wish not found")
    return wish


@router.post("/", response_model=schemas.Wish, status_code=status.HTTP_201_CREATED)
def create_wish(
    wish: schemas.WishCreate,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(auth.get_current_user),
):
    return crud.create_wish(db, wish)


@router.put("/{wish_id}", response_model=schemas.Wish)
def update_wish(
    wish_id: int,
    wish: schemas.WishUpdate,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(auth.get_current_user),
):
    updated_wish = crud.update_wish(db, wish_id, wish)
    if updated_wish is None:
        raise HTTPException(status_code=404, detail="Wish not found")
    return updated_wish


@router.delete("/{wish_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wish(
    wish_id: int,
    db: Session = Depends(database.get_db),
    current_user: str = Depends(auth.get_current_user),
):
    success = crud.delete_wish(db, wish_id)
    if not success:
        raise HTTPException(status_code=404, detail="Wish not found")
    return {"detail": "Wish deleted successfully"}
