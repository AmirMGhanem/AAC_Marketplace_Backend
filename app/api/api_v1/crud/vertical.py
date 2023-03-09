from sqlalchemy.orm import Session

from app.db.model_db import TVertical, TVerticalfield


def get_verticals(db: Session):
    return db.query(TVertical).all()

def get_vertical(db: Session, vertical_id: int):
    return db.query(TVertical).filter(TVertical.vertical_id == vertical_id).first()


def get_vertical_fields(db: Session, vertical_id: int):
    return db.query(TVerticalfield).filter((TVerticalfield.verticalfields_vertical_id == vertical_id) | (
                TVerticalfield.verticalfields_vertical_id == 0)).all()
