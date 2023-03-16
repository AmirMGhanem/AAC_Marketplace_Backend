import json

from fastapi import APIRouter, File, UploadFile, BackgroundTasks, Depends, Form
from sqlalchemy.orm import Session

from app.api.api_v1.crud.vertical import get_vertical_fields_with_answers_only
from app.mylogger import mylogger
from app.utils.NLP import find_best_score_similarity
from app.utils.files import save_file
from app.utils.generate import random_id
import os
import pandas as pd
import numpy as np
from app.db.session import get_db

logger = mylogger(__name__)

router = APIRouter()
db= get_db()

@router.post("/uploadfile/")
def create_upload_file(background_tasks: BackgroundTasks,headers:list = Form(...),file: UploadFile = File(...)):
    headers = headers[0].split(",")
    id=random_id(100,9999)
    background_tasks.add_task(save_file,id,file)
    predicted_fields={}
    generic_mapper_path=os.path.join(os.getcwd(),"app",  "assets", "files","fields_map", "generic_fields_map.json")

    with open(generic_mapper_path,"r") as f:
        generic_mapper = json.load(f)
        for col in headers:
            key=find_best_score_similarity(col, generic_mapper.keys())
            predicted_fields[key]=col
            for key in generic_mapper:
                if col in generic_mapper[key]:
                    predicted_fields[key]=col
    return {"filename": file.filename, "id": id, "predicted_fields": predicted_fields}

@router.post("/fields_values")
def read_fields_values(payload:dict,db: Session = Depends(get_db)):
    unique_values = {}
    file_id=payload['file_id']
    mapped_headers=payload['data']
    filename = str(file_id) + ".csv"
    file_path = os.path.join(os.getcwd(), "app", "assets", "files", filename)
    df = pd.read_csv(file_path)
    result = get_vertical_fields_with_answers_only(db)
    mapped_values = {}
    generic_mapper_path=os.path.join(os.getcwd(), "app", "assets", "files","fields_map", "generic_fields_map.json")

    with open(generic_mapper_path, 'r+') as f:
        json_data = json.load(f)
        for key, value in mapped_headers.items():
            if value not in json_data[key] and value != "" and value is not None:
                json_data[key].append(value)
                f.seek(0)
                json.dump(json_data, f, indent=4)
                f.truncate()

            if key in result and value is not None and value != "":
                mapped_values[key] = value
        print(df.columns)
        for column in df.columns:

            if column in mapped_values.values():
                key = list(mapped_values.keys())[list(mapped_values.values()).index(column)]
                unique_values[column] = np.unique(df[column].dropna().values).tolist()
        f.close()
    return unique_values


