
from sqlalchemy.orm import Session
import hashlib
from app.api.api_v1.models.user import UserDB


def login(db: Session, user_name: str, user_password: str):
    hashed_user_password = hashlib.md5(user_password.encode()).hexdigest()
    print(hashed_user_password)
    db_user = db.query(UserDB).filter(UserDB.user_name == user_name).filter(UserDB.user_password == hashed_user_password).first()
    return db_user

