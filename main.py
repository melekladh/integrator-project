from fastapi import FastAPI
from pydantic import BaseModel
from utils.init_chroma import init_chroma
from utils.search import search_documents
from utils.generate import generate_answer

# Initialisation de l'application
app = FastAPI()

# Initialiser la collection ChromaDB
collection = init_chroma()

# Définition de l'endpoint GET /
@app.get("/")
async def read_root():
    return {
        "version": "1.0.0",
        "swagger": "/docs"
    }

class SearchRequest(BaseModel):
    query: str

@app.post("/search")
def search_api(request: SearchRequest):
    documents = search_documents(collection, request.query)

    return {
        "query": request.query,
        "top_documents": documents
    }

@app.post("/generate")
def generate_api(request: SearchRequest):
    """Generate an answer based on search results"""
    # Get relevant documents
    documents = search_documents(collection, request.query, k=5)
    
    # Generate answer using the documents
    answer = generate_answer(request.query)
    
    return {
        "query": request.query,
        "answer": answer,
        "source_documents": documents
    }
