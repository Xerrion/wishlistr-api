# app/router/users.py
from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app import database
from app.api.deps import SessionDep, AdminUser, CurrentUser
from app.crud import user as user_crud
from app.database import get_session
from app.models.user import Role, User, UserCreate, UserRead, UserUpdate

router = APIRouter()


@router.post("/", response_model_exclude={"password"})
def create_user(
    *,
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
    current_user: CurrentUser,
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
    user_id: int,
    session: SessionDep,
    is_admin: AdminUser,
) -> UserUpdate:
    updated_user = user_crud.update(session=session, user_id=user_id)

    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserUpdate.model_validate(updated_user)


# Endpoint to delete a user
@router.delete("/{user_id}")
def delete_user(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    user_id: int,
) -> Response:
    if current_user.id != user_id or not current_user.role != Role.ADMIN:
        raise HTTPException(status_code=401, detail="Not enough permissions")

    deleted_user = user_crud.delete(user_id=user_id, session=session)

    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(content={"detail": "User deleted successfully"})
