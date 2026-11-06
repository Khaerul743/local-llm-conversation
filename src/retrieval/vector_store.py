from langchain_chroma import Chroma

from src.config.settings import settings
from src.ingestion.embedding import EmbeddingService


class VectorStore:
    def __init__(self):
        self._embedding_service = EmbeddingService()
        self.vector_store = Chroma(
            collection_name="knowledge_base",
            embedding_function=self._embedding_service.get_embedding_model(),
            persist_directory=settings.CHROMA_PATH,
        )

    def add_documents(self, documents):
        if not documents:
            raise ValueError("No documents to store")

        self.vector_store.add_documents(documents=documents)

    def similarity_search(self, query: str, k: int = 4):
        return self.vector_store.similarity_search(query=query, k=k)
