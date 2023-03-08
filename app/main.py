from fastapi import FastAPI
from app.api.api_v1.api import api_router
from app.core.config import get_settings
from app.db.session import engine
from app.db.base import Base
from fastapi.middleware.cors import CORSMiddleware
from app.middleware.api_calls_middleware import api_calls_middleware


import uvicorn



Base.metadata.create_all(bind=engine)

app = FastAPI(title=get_settings().PROJECT_NAME)
origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:3000",
    "http://localhost:55813",
    ]



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# add middleware function to app
api_calls_middleware(app)



app.include_router(api_router, prefix=get_settings().API_V1_STR)


if __name__ == "__main__":
    uvicorn.run("__main__:app", host="0.0.0.0", port=8000, reload=True, workers=2)
