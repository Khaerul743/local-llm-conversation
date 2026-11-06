from src.ingestion.loader import DocumentLoader
from src.ingestion.splitter import DocumentSplitter
from src.retrieval.vector_store import VectorStore


class IngestionService:
    def __init__(self):
        self.document_loader = DocumentLoader()
        self.document_splitter = DocumentSplitter()
        self.vector_store = VectorStore()

    def ingest(self, file_path: str):
        # 1. Load document
        documents = self.document_loader.load(file_path)

        if not documents:
            raise ValueError("Document contains no extractable text.")

        # 2. Split document
        chunks = self.document_splitter.split(documents)

        # 3. Store chunks and generate embeddings
        self.vector_store.add_documents(chunks)

        return {
            "filename": file_path,
            "total_documents": len(documents),
            "total_chunks": len(chunks),
            "status": "success",
        }
