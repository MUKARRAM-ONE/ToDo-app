from pydantic import BaseModel, EmailStr
from typing import Optional

class UserSignUp(BaseModel):
    email: EmailStr
    password: str
    name: str

class UserSignIn(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: str
    email: str
    name: str

class Token(BaseModel):
    access_token: str
    token_type: str
    user: UserResponse
