from src.services.ingestion_service import IngestionService

ingestion_service = IngestionService()
# ingestion_service.ingest("./documents/Sejarah_Filsafat.pdf")

result = ingestion_service.vector_store.similarity_search("Helo apa kabar?", k=1)
print(result)
