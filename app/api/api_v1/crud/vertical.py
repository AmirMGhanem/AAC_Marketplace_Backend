from sqlalchemy.orm import Session

from app.db.model_db import TVertical


def get_verticals(db: Session):
    return db.query(TVertical).all()

def get_vertical(db: Session, vertical_id: int):
    return db.query(TVertical).filter(TVertical.vertical_id == vertical_id).first()
