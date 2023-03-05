from typing import Optional
# Pydantic
from pydantic import BaseModel


class User(BaseModel):
    user_id: Optional[int]
    user_name: Optional[str]
    user_login: Optional[str]
    user_company_id: Optional[int]
    user_role_id: Optional[int]



    class Config:
        orm_mode = True
