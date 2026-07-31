import os

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    CSVLoader,
    Docx2txtLoader
)


def load_document(documents):

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", documents.name)

    with open(file_path, "wb") as f:
        f.write(documents.getbuffer())

    extension = documents.name.split(".")[-1].lower()

    if extension == "pdf":
        loader = PyPDFLoader(file_path)

    elif extension == "txt":
        loader = TextLoader(file_path)

    elif extension == "docx":
        loader = Docx2txtLoader(file_path)

    elif extension == "csv":
        loader = CSVLoader(file_path)

    else:
        raise ValueError("Unsupported file type")

    return loader.load()