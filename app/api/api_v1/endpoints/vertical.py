
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.api.api_v1.models.vertical import Vertical
from app.db.session import get_db
from app.api.api_v1.crud.vertical import get_verticals, get_vertical


router = APIRouter()
db= get_db()



@router.get("/get_all", response_model=List[Vertical])
def find_user(db: Session = Depends(get_db)):
    db_user = get_verticals(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
