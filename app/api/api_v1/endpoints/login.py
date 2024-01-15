# app/router/users.py
from fastapi import APIRouter, HTTPException
from starlette import status

from app.api.deps import SessionDep, FormDataDep
from app.core import security
from app.models.user import Token

router = APIRouter()


@router.post("/")
def login_for_access_token(
    *,
    session: SessionDep,
    form_data: FormDataDep,
) -> Token:
    user = security.authenticate_user(form_data.username, form_data.password, session)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = security.create_access_token(subject=user.username)
    token_data = Token(access_token=access_token, token_type="bearer")
    return Token.model_validate(token_data)


# @router.post("/token/refresh")
# def refresh_access_token(
#     session: SessionDep,
#     refresh_token: TokenDep,
# ) -> Token:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     username = security.verify_refresh_token(refresh_token, credentials_exception)
#     user =  user_crud.read_by_username(username=username, session=session)
#     if not user:
#         raise credentials_exception
#     access_token = security.create_access_token(data={"sub": user.username})
#     token_data = Token(access_token=access_token, token_type="bearer")
#     return Token.model_validate(token_data)
