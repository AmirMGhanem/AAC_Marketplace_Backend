from sqlalchemy.orm import Session
import hashlib
from app.db.model_db import TUser
from app.utils.generate import get_token


def login(db: Session, user_login: str, user_password: str):
    hashed_user_password = hashlib.md5(user_password.encode()).hexdigest()
    db_user = db.query(TUser).with_entities(TUser.user_login, TUser.user_name, TUser.user_company, TUser.user_role_id, TUser.user_id).filter(TUser.user_login == user_login).filter(TUser.user_password == hashed_user_password).first()
    if db_user is not None:
        db_user = db_user._asdict()
        db_user = get_token(db_user)
        return db_user
    else:
        return None
