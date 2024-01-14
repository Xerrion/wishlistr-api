from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer, APIKeyHeader
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlmodel import Session

from app.core.config import settings
from app.crud import user as user_crud
from app.models.user import TokenPayload

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/")
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
api_key_header = APIKeyHeader(name="X-API-Key")


def create_access_token(subject: str, expires_delta: timedelta = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"exp": expire, "sub": subject}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenPayload(username=username)
    except JWTError:
        raise credentials_exception
    return token_data.model_validate(token_data)


def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, session: Session):
    user = user_crud.read_by_username(username=username, session=session)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
