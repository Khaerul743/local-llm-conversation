from src.ingestion.loader import DocumentLoader

document_loader = DocumentLoader()
documents = document_loader.load("./documents/Sejarah_Filsafat.pdf")

print(documents)
