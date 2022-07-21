from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):
    csv_file_name: str
    db_name: str

    class Config:
        env_file = Path(__file__).parent.parent.parent / ".env"


config = Settings()