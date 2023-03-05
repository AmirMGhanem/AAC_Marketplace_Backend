from typing import Optional

# Pydantic
from pydantic import BaseModel


class Vertical(BaseModel):
    vertical_id: Optional[int]
    vertical_name: Optional[str]
    class Config:
        orm_mode = True