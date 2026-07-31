import os
from dotenv import load_dotenv
from langchain_cohere import CohereEmbeddings

# Load .env file
load_dotenv()

COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not COHERE_API_KEY:
    raise ValueError("COHERE_API_KEY not found in .env file")


def get_embeddings():
    """
    Return a Cohere Embeddings object.
    """

    embeddings = CohereEmbeddings(
        model="embed-english-v3.0",
        cohere_api_key=COHERE_API_KEY
    )

    return embeddings