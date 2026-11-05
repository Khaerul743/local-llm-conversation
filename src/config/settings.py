from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    APP_NAME: str = "local llm conversation"
    LLM_MODE: Literal["local","public"]
    LLM_MODEL: str

    class Config:
        env_file = ".env"

settings = Settings()