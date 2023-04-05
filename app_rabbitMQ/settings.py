import os
from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):



    rabbit_dsn: str = os.getenv('RABBITMQ_DSN', '')
    DSN_MINIO: str = os.getenv('DSN_MINIO', '')
    MINIO_ACCESS_KEY: str = os.getenv('MINIO_ACCESS_KEY', '')
    MINIO_SECRET_KEY: str = os.getenv('MINIO_SECRET_KEY', '')
    TELEGRAM_TOKEN: str = os.getenv('TELEGRAM_TOKEN', '')


    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
