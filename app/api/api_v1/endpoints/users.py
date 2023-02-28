from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.api.api_v1.models.user import User
from app.db.session import get_db
from app.api.api_v1.crud.user import get_user, get_users


router = APIRouter()
db= get_db()



@router.get("/user", response_model=User)
def find_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.get("/users/", response_model=List[User])
def find_users(db: Session = Depends(get_db)):
    db_users = get_users(db)
    if db_users is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return db_users
