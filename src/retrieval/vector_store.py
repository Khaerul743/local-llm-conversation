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
        result = self.vector_store.similarity_search(query=query, k=k)
        return result

    def list_documents(self):
        stored = self.vector_store.get(include=["metadatas"])
        documents = {}

        for metadata in stored["metadatas"] or []:
            source = metadata.get("source", "Dokumen tanpa sumber")
            filename = source.replace("\\", "/").rsplit("/", 1)[-1]
            documents[source] = documents.get(
                source, {"filename": filename, "chunks": 0}
            )
            documents[source]["chunks"] += 1

        return list(documents.values())
