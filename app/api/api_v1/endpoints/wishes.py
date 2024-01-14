# app/routers/wishes.py

from fastapi import APIRouter, HTTPException, status

from app.api.deps import SessionDep, CurrentUser
from app.crud import wish as wish_crud
from app.crud import wishlist as wishlist_crud
from app.models.wish import WishUpdate, WishCreate

router = APIRouter()


@router.get("/")
def read_wishes(*, skip: int = 0, limit: int = 100, wishlist_id: int = None, session: SessionDep):
    if wishlist_id:
        return wishlist_crud.read_by_wishlist(session, skip, limit, wishlist_id)
    return wish_crud.read_all(session, skip, limit)


@router.get("/{wish_id}")
def read_wish(*, wish_id: int, session: SessionDep):
    wish = wish_crud.read(session, wish_id)
    if wish is None:
        raise HTTPException(status_code=404, detail="Wish not found")
    return wish


# Endpoint to create a wish within a specific wishlist
@router.post("/")
def create_wish(*, wish: WishCreate, session: SessionDep, current_user: CurrentUser):  # Assuming user authentication
    # Check if the specified wishlist exists
    if not wishlist_crud.read(session, wish.wishlist_id):
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return wish_crud.create(session, wish)


# Endpoint to update a wish
@router.put("/{wish_id}")
def update_wish(*, wish_id: int, wish: WishUpdate, session: SessionDep, current_user: CurrentUser):
    updated_wish = wish_crud.update(session, wish_id, wish)
    if updated_wish is None:
        raise HTTPException(status_code=404, detail="Wish not found")
    return updated_wish


@router.delete("/{wish_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_wish(*, wish_id: int, session: SessionDep, current_user: CurrentUser):
    success = wish_crud.delete(session, wish_id)
    if not success:
        raise HTTPException(status_code=404, detail="Wish not found")
    return {"detail": "Wish deleted successfully"}
