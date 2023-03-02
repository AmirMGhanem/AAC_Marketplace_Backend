
from sqlalchemy.orm import Session
import hashlib
from app.db.model_db import TUser


def login(db: Session, user_login: str, user_password: str):
    hashed_user_password = hashlib.md5(user_password.encode()).hexdigest()
    db_user = db.query(TUser).filter(TUser.user_login == user_login).filter(TUser.user_password == hashed_user_password).first()
    return db_user

