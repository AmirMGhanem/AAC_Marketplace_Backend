from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Header,Request
from sqlalchemy.orm import Session
from app.api.api_v1.models.auth import UserAuth, UserLogin
from app.db.session import get_db
from app.api.api_v1.crud.auth import login
from app.api.api_v1.crud.user import get_user_by_token

router = APIRouter()
db = get_db()


@router.post("/login", response_model=dict)
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    db_user = login(db, user_login=user.user_login, user_password=user.user_password)
    if db_user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return {"token": db_user}


@router.get("/user", response_model=UserAuth)
def get_user(req: Request,db: Session = Depends(get_db)):
    token = req.headers["Authorization"]

    db_user=get_user_by_token(db,token)
    if db_user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return db_user
