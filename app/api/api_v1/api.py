from fastapi import APIRouter
from app.api.api_v1.endpoints import auth, users, vertical, files,answer,test

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(vertical.router, prefix="/vertical", tags=["vertical"])
api_router.include_router(files.router, prefix="/files", tags=["file"])
api_router.include_router(answer.router, prefix="/answers", tags=["answer"])
api_router.include_router(test.router, prefix="/test", tags=["test"])