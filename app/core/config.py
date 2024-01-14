import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, HttpUrl, PostgresDsn, validator, field_validator, Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "din_mor_stor"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SERVER_NAME: str = "localhost"
    SERVER_HOST: AnyHttpUrl = Field("http://localhost", validate_default=True)
    BACKEND_CORS_ORIGINS: List[str] = ["*"]
    ALGORITHM: str = "HS256"

    @field_validator("BACKEND_CORS_ORIGINS")
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = Field("Wislistr", validate_default=True)

    # POSTGRES_SERVER: str
    # POSTGRES_USER: str
    # POSTGRES_PASSWORD: str
    # POSTGRES_DB: str
    SQLITE_DB: str = "sqlite:///./sql_app.db"
    SQLALCHEMY_DATABASE_URI: str = Field(default=SQLITE_DB, env="DATABASE_URL")

    class Config:
        case_sensitive = True


settings = Settings()
