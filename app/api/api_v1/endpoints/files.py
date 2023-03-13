
from fastapi import APIRouter, File, UploadFile
from app.mylogger import mylogger
logger = mylogger(__name__)
from app.db.session import get_db

router = APIRouter()
db= get_db()

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    while file.current_upload_size < file.content_length:
        print(f"Uploaded {file.current_upload_size} of {file.content_length} bytes")
    return {"filename": file.filename, "contents": contents}
