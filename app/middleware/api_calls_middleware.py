from fastapi import FastAPI
from starlette.requests import Request
from ..settings import mylogger
from ..utils.generate import decode_token


logger = mylogger(__name__)

def api_calls_middleware(app: FastAPI):
    @app.middleware("http")
    async def middleware(request: Request, call_next):
        ip = request.client.host
        if request.headers.get("Authorization"):
            token = request.headers.get("Authorization")
            user = decode_token(token)
            logger.middleware_log(f"User {user['user_login']} called {request.url} from {ip}")
        else:
            logger.middleware_log(f"Anonymous user called {request.url} from {ip}")
        response = await call_next(request)
        return response