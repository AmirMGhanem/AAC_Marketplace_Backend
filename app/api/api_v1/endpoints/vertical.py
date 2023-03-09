
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.mylogger import mylogger
logger = mylogger(__name__)
from app.api.api_v1.models.vertical import Vertical,VerticalFields
from app.db.session import get_db
from app.api.api_v1.crud.vertical import get_verticals,get_vertical_fields


router = APIRouter()
db= get_db()



@router.get("/get_all", response_model=List[Vertical])
def get_all_verticals(db: Session = Depends(get_db)):
    db_user = get_verticals(db)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/get_fields/{id}", response_model=List[VerticalFields])
def get_vertical_fields_func(id: int, db: Session = Depends(get_db)):
    db_user = get_vertical_fields(db, id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user