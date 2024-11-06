from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional
from typing_extensions import Annotated

from pydantic import BaseModel, Field


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
    username: str
    password: str


# Setting up a schema for the token

class Token(BaseModel):
    access_token: str
    token_type: str
    
class TokenData(BaseModel):
    id: Optional[str] = None
    # id: str | None = None

