# app/router/users.py
from fastapi import APIRouter, HTTPException, Response
from fastapi.responses import JSONResponse

from app.api.deps import SessionDep, AdminUser
from app.crud import user as user_crud
from app.models.user import UserCreate, UserRead, UserUpdate

router = APIRouter()


@router.post("/", response_model_exclude={"password"})
def create_user(
    *,
    is_admin: AdminUser,
    session: SessionDep,
    user: UserCreate,
) -> UserRead:
    db_user = user_crud.read_by_username(session=session, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = user_crud.create(session=session, user=user)
    return UserRead.model_validate(new_user)


@router.get("/{user_id}", response_model_exclude={"password", "role"})
def read_user(
    *,
    is_admin: AdminUser,
    session: SessionDep,
    user_id: int,
) -> UserRead:
    db_user = user_crud.read(user_id=user_id, session=session)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return UserRead.model_validate(db_user)


# Endpoint to update a user
@router.put("/{user_id}")
def update_user(
    *,
    is_admin: AdminUser,
    session: SessionDep,
    user_id: int,
) -> UserUpdate:
    updated_user = user_crud.update(session=session, user_id=user_id)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserUpdate.model_validate(updated_user)


# Endpoint to delete a user
@router.delete("/{user_id}")
def delete_user(
    *,
    is_admin: AdminUser,
    session: SessionDep,
    user_id: int,
) -> Response:
    deleted_user = user_crud.delete(user_id=user_id, session=session)

    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(content={"detail": "User deleted successfully"})
