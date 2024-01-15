from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from starlette import status

from app import database, crud
from app.core import security
from app.models.user import User, Role

SessionDep = Annotated[Session, Depends(database.get_session)]
TokenDep = Annotated[str, Depends(security.oauth2_scheme)]
ApiKeyDep = Annotated[str, Depends(security.api_key_header)]
FormDataDep = Annotated[OAuth2PasswordRequestForm, Depends()]
AdminDep = Annotated[bool, Depends()]


def get_current_user(session: SessionDep, token: ApiKeyDep) -> User:
    token_data = security.verify_token(
        token,
        credentials_exception=HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ),
    )

    user = crud.user.read_by_username(username=token_data.username, session=session)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]


def get_current_user_admin(current_user: CurrentUser) -> User:
    if not current_user.role == Role.ADMIN:
        raise HTTPException(status_code=400, detail="The user doesn't have enough privileges")
    return current_user


AdminUser = Annotated[User, Depends(get_current_user_admin)]
