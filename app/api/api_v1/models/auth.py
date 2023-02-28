from typing import Optional, List
from sqlalchemy import Column, Integer, String
from app.db.base import Base
# Pydantic
from pydantic import BaseModel



class UserAuth(BaseModel):
    user_id: Optional[int]
    user_name: Optional[str]
    user_login: Optional[str]
    user_company_id: Optional[int]
    user_role_id: Optional[int]
    user_password: Optional[str]


    class Config:
        orm_mode = True