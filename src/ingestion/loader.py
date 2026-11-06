from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader

class DocumentLoader:

    def load(self, file_path: str):
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        extention = path.suffix.lower()
        if extention == ".pdf":
            loader = PyPDFLoader(
                str(path),
                mode="page"
            )

        elif extention == "txt":
            loader = TextLoader(
                str(path),
                encoding="utf-8"
            )

        else:
            raise ValueError(
                f"Unsupport file type: {extention}"
            )

        documents = loader.load()

        documents = [
            doc for doc in documents if doc.page_content.strip()
        ]

        return documents