from sqlalchemy.orm import Session
from app.db.model_db import TAnswer



def fields_answers(db: Session):
    return db.query(TAnswer).all()

