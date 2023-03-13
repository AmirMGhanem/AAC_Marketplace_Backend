from typing import Optional, List

from pydantic import BaseModel


class Answers(BaseModel):
    answer_id: Optional[int]
    answer_verticalfield_id: Optional[int]
    answer_verticalfield_choice: Optional[str]
    answer_verticalfield_answer: Optional[str]

    class Config:
        orm_mode = True