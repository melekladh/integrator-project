def search_documents(collection, query: str, k: int = 5):
    """
    Search top-k relevant documents from ChromaDB
    """
    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    # results["documents"] is a list of lists
    documents = results["documents"][0]

    return documents
