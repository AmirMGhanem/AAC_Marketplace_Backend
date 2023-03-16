from typing import Optional, List

# Pydantic
from pydantic import BaseModel

from app.api.api_v1.models.answer import Answers


class Vertical(BaseModel):
    vertical_id: Optional[int]
    vertical_name: Optional[str]
    class Config:
        orm_mode = True



class VerticalFields(BaseModel):
    verticalfields_id: Optional[int]
    verticalfields_vertical_id: Optional[str]
    verticalfields_example: Optional[str]
    verticalfields_fieldname: Optional[str]
    verticalfields_pattern: Optional[str]
    verticalfields_mandatory: Optional[int]



class VerticalFieldsWithAnswers(BaseModel):
    verticalfields_id: Optional[int]
    verticalfields_vertical_id: Optional[str]
    verticalfields_fieldname: Optional[str]
    verticalfields_pattern: Optional[str]
    verticalfields_mandatory: Optional[int]
    verticalfields_example: Optional[str]
    answers: Optional[List[Answers]]

    class Config:
        orm_mode = True