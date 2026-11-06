from src.ingestion.loader import DocumentLoader
from src.ingestion.splitter import DocumentSplitter

document_loader = DocumentLoader()
document_splitter = DocumentSplitter()

documents = document_loader.load("./documents/Sejarah_Filsafat.pdf")
split = document_splitter.split(documents)
print(split)
