from sqlalchemy.orm import Session

from app.api.api_v1.models.user import UserDB

def get_user(db: Session, user_id: int):
    return db.query(UserDB).filter(UserDB.user_id == user_id).first()

def get_users(db: Session):
    return db.query(UserDB).all()

