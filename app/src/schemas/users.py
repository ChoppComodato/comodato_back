from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict, EmailStr, constr

r_phone = r"^\d{10,15}$"

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    username: str
    email: EmailStr
    created_at: datetime



class UserCreate(BaseModel):
    username: str
    password: str
    email: EmailStr
    phone: constr(pattern=r_phone)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None