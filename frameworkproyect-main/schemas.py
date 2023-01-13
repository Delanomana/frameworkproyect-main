from pydantic import BaseModel
from typing import Optional

class UserRequestModel(BaseModel):
    username: str
    email: str
    password: str

class UserRequestModel(BaseModel):
    username: str
    email: str

class UserResponseModel(UserRequestModel):
    id: int 
