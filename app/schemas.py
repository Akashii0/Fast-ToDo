from datetime import datetime
# from typing import Optional

from fastapi import Form
from pydantic import BaseModel
# from typing_extensions import Annotated


class UserCreate(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    id: int
    username: str
    created_at: datetime

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    username: str = Form()
    password: str = Form()


# Setting up a schema for the token


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None = None
    # id: Optional[str] = None
