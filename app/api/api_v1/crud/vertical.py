from sqlalchemy.orm import Session

from app.db.model_db import TVertical, TVerticalfield


def get_verticals(db: Session):
    return db.query(TVertical).all()

def get_vertical(db: Session, vertical_id: int):
    return db.query(TVertical).filter(TVertical.vertical_id == vertical_id).first()


def get_vertical_fields(db: Session, vertical_id: int):
    return db.query(TVerticalfield).filter((TVerticalfield.verticalfields_vertical_id == vertical_id) | (
                TVerticalfield.verticalfields_vertical_id == 0)).all()



def get_vertical_fields_with_answers(db: Session, vertical_id: int):
    result= db.query(TVerticalfield).filter((TVerticalfield.verticalfields_vertical_id == vertical_id) | (TVerticalfield.verticalfields_vertical_id == 0)).all()
    return result


def get_vertical_fields_with_answers_only(db: Session):
    result= db.query(TVerticalfield).all()
    result = list(filter(lambda x: x if len(x.answers)>0 else None, result))
    result = list(map(lambda x: x.verticalfields_fieldname, result))
    return result


