
from fastapi import APIRouter, File, UploadFile,BackgroundTasks
from app.mylogger import mylogger
from app.utils.files import save_file
from app.utils.generate import random_id
import os
import csv


logger = mylogger(__name__)
from app.db.session import get_db

router = APIRouter()
db= get_db()

@router.post("/uploadfile/")
def create_upload_file(background_tasks: BackgroundTasks,file: UploadFile = File(...)):
    id=random_id(100,9999)
    background_tasks.add_task(save_file,id,file)
    return {"filename": file.filename, "id": id}

@router.get("/fields_values/{id}")
def read_fields_values(id: int):
    filename = str(id) + ".csv"
    file_path = os.path.join(os.getcwd(), "app", "assets", "files", filename)
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        rows = []
        keys = set()  # Use a set to store unique keys
        new_row = {}
        for row in reader:
            rows.append(row)

        for row in rows:
            for key in row:
                if key not in keys:
                    keys.add(key)
                    new_row[key] = set()
                new_row[key].add(row[key])

        return new_row


