from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.config.settings import settings

class DocumentSplitter:
    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
            add_start_index=True,
        )


    def split(self, documents):
        chunks = self.splitter.split_documents(
            documents
        )

        return chunks