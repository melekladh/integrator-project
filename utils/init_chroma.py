import chromadb
from chromadb.config import Settings

def init_chroma(collection_name="faq_chatbot"):
    """
    Initialize ChromaDB and create collection
    """
    client = chromadb.Client(
        Settings(
            persist_directory="./chroma_db",
            anonymized_telemetry=False
        )
    )

    collection = client.get_or_create_collection(name=collection_name)
    return collection
