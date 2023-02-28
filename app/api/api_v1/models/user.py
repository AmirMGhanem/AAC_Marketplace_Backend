from typing import Optional, List
from sqlalchemy import Column, Integer, String
from app.db.base import Base
# Pydantic
from pydantic import BaseModel

class UserDB(Base):
    __tablename__ = "T_user"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True, index=True)
    user_company_id=Column(Integer)
    user_login = Column(String)
    user_password = Column(String)
    user_role_id = Column(Integer)


class User(BaseModel):
    user_id: Optional[int]
    user_name: Optional[str]
    user_login: Optional[str]
    user_company_id: Optional[int]
    user_role_id: Optional[int]


    class Config:
        orm_mode = True