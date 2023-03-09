from typing import Optional

# Pydantic
from pydantic import BaseModel


class Vertical(BaseModel):
    vertical_id: Optional[int]
    vertical_name: Optional[str]
    class Config:
        orm_mode = True



class VerticalFields(BaseModel):
    verticalfields_id: Optional[int]
    verticalfields_vertical_id: Optional[str]
    verticalfields_fieldname: Optional[str]
    verticalfields_pattern: Optional[str]
    verticalfields_mandatory: Optional[int]
    class Config:
        orm_mode = True