from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import get_settings
from app.db.session import engine
from app.db.base import Base
import uvicorn


Base.metadata.create_all(bind=engine)

app = FastAPI(title=get_settings().PROJECT_NAME)

app.include_router(api_router, prefix=get_settings().API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
