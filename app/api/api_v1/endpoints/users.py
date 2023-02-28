from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.api_v1.models.user import User, UserCreate
from app.db.session import get_db
from app.api.api_v1.crud.user import get_user_by_email, create_user,get_users

router = APIRouter()
db= get_db()

@router.post("/users/", response_model=User)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db, user)

@router.get("/users", response_model=User)
def read_user(db: Session = Depends(get_db)):
    db_user = get_users(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
