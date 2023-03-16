from sqlalchemy.orm import Session
from app.db.model_db import TAnswer


def fields_answers(db: Session):
    result= db.query(TAnswer).all()
    return result




