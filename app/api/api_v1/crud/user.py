from sqlalchemy.orm import Session

from app.db.model_db import TUser

def get_user(db: Session, user_id: int):
    return db.query(TUser).filter(TUser.user_id == user_id).first()

def get_users(db: Session):
    return db.query(TUser).all()



