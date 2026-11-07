from typing import Literal

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "local llm conversation"

    OLLAMA_HOST: str = "http://localhost:11434"

    LLM_PROVIDER: Literal["local", "openai"]
    LLM_MODEL: str
    LLM_TEMPERATURE: float
    EMBEDDING_MODEL: str

    CHROMA_PATH: str
    CHUNK_SIZE: int
    CHUNK_OVERLAP: int

    OPENAI_API_KEY: str | None = None

    class Config:
        env_file = ".env"


settings = Settings()
