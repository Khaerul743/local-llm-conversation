from langchain.tools import tool

from src.retrieval.vector_store import VectorStore

vectore_store = VectorStore()


@tool
def retrieve_document(query: str) -> list:
    """
    to retrieve document knowledge
    """
    result = vectore_store.similarity_search(query, k=2)
    return result
