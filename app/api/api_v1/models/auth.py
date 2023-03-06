from typing import Optional, List
# Pydantic
from pydantic import BaseModel

class UserLogin(BaseModel):
    user_login: str
    user_password: str

class UserAuth(BaseModel):
    user_id: Optional[int]
    user_name: Optional[str]
    user_login: Optional[str]
    user_company_id: Optional[int]
    user_role_id: Optional[int]


    class Config:
        orm_mode = True