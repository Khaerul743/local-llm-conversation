from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    APP_NAME: str = "local llm conversation"

    OLLAMA_HOST: str = "http://localhost:11434"
    
    LLM_MODE: Literal["local","public"]
    LLM_MODEL: str
    LLM_TEMPERATURE: float

    class Config:
        env_file = ".env"

settings = Settings()