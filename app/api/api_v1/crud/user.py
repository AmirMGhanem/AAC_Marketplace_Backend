from sqlalchemy.orm import Session
from app.utils.generate import decode_token
from app.db.model_db import TUser

def get_user(db: Session, user_id: int):
    return db.query(TUser).filter(TUser.user_id == user_id).first()


def get_user_by_token(db: Session, token: str):
    user= decode_token(token)
    return db.query(TUser).filter(TUser.user_id == user['user_id']).first()



def get_users(db: Session):
    return db.query(TUser).all()



