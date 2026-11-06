from langchain_ollama import OllamaEmbeddings

from src.config.settings import settings


class EmbeddingService:
    def __init__(self):
        self.embedding = OllamaEmbeddings(
            model=settings.EMBEDDING_MODEL, base_url=settings.OLLAMA_HOST
        )

    def get_embedding_model(self):
        return self.embedding
