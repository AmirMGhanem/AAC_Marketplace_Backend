from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "AAC Marketplace"
    API_V1_STR: str = "/api/v1"
    SQLALCHEMY_DATABASE_URI: str = "mysql+pymysql://amir:Quc%N6FUA5E%40axlT1xD3fm@ps13.lmal.me/db_marketplace"


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    return Settings()
