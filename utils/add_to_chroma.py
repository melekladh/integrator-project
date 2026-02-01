import uuid

def add_documents_to_chroma(collection, documents):
    """
    Insert documents individually into ChromaDB
    """
    ids = [str(uuid.uuid4()) for _ in documents]

    collection.add(
        documents=documents,
        ids=ids
    )
