# In app/routers/wishlists.py

from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep, AdminUser
from app.crud import wishlist as wishlist_crud
from app.models.wishlist import WishlistCreate, WishlistUpdate

router = APIRouter()


@router.post("/")
def create_wishlist(
    *,
    is_admin: AdminUser,
    session: SessionDep,
    wishlist: WishlistCreate,
):
    return wishlist_crud.create(session, wishlist=wishlist)


@router.get("/")
def read_wishlists(
    *,
    session: SessionDep,
    skip: int = 0,
    limit: int = 100,
):
    return wishlist_crud.read_all(session, skip=skip, limit=limit)


@router.get("/{wishlist_id}")
def read_wishlist(
    *,
    session: SessionDep,
    wishlist_id: int,
):
    wishlist = wishlist_crud.read(session, wishlist_id=wishlist_id)
    if wishlist is None:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return wishlist


@router.put("/{wishlist_id}")
def update_wishlist(
    *,
    is_admin: AdminUser,
    session: SessionDep,
    wishlist_id: int,
    wishlist: WishlistUpdate,
):
    updated_wishlist = wishlist_crud.update(session, wishlist_id=wishlist_id, wishlist=wishlist)
    if updated_wishlist is None:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return updated_wishlist


@router.delete("/{wishlist_id}")
def delete_wishlist(
    *,
    is_admin: AdminUser,
    session: SessionDep,
    wishlist_id: int,
):
    wishlist = wishlist_crud.delete(session, wishlist_id=wishlist_id)
    if wishlist is None:
        raise HTTPException(status_code=404, detail="Wishlist not found")
    return wishlist
