
from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.mylogger import mylogger
from app.api.api_v1.models.answer import Answers
from app.api.api_v1.crud.answer import fields_answers
from sqlalchemy.orm import Session


logger = mylogger(__name__)
from app.db.session import get_db

router = APIRouter()
db= get_db()

@router.get("/get_all/",response_model=List[Answers])
def get_all_answer(db: Session = Depends(get_db)):
    logger.info("get_all_answer")
    db_answer = fields_answers(db)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_answer

