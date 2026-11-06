from pydantic_settings import BaseSettings
from typing import Literal

class Settings(BaseSettings):
    APP_NAME: str = "local llm conversation"

    OLLAMA_HOST: str = "http://localhost:11434"
    
    LLM_PROVIDER: Literal["local","openai"]
    LLM_MODEL: str
    LLM_TEMPERATURE: float
    EMBEDDING_MODEL: str

    CHUNK_SIZE: int
    CHUNK_OVERLAP: int
    
    class Config:
        env_file = ".env"

settings = Settings()