
from sqlalchemy.orm import Session
import hashlib
from app.api.api_v1.models.user import UserDB


def login(db: Session, user_login: str, user_password: str):
    hashed_user_password = hashlib.md5(user_password.encode()).hexdigest()
    db_user = db.query(UserDB).filter(UserDB.user_login == user_login).filter(UserDB.user_password == hashed_user_password).first()
    return db_user

