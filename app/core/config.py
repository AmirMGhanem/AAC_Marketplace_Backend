from functools import lru_cache
from pydantic import BaseSettings

# change config according to user
# TODO: to run mongo locally download studio3t
# MONGOALCHEMY_DATABASE_URI: str = "mongodb://localhost:27017/"


class Settings(BaseSettings):
    PROJECT_NAME: str = "AAC Marketplace"
    API_V1_STR: str = "/api/v1"
    #SQLALCHEMY_DATABASE_URI: str = "mysql+pymysql://amir:Quc%N6FUA5E%40axlT1xD3fm@ps13.lmal.me/db_marketplace"
    SQLALCHEMY_DATABASE_URI: str = "mysql+pymysql://root:@localhost/test"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

@lru_cache()
def get_settings():
    return Settings()
