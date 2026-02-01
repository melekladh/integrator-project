from utils.load_data import load_data
from utils.init_chroma import init_chroma   
from utils.add_to_chroma import add_documents_to_chroma 
from utils.search import search_documents
from utils.generate import generate_answer
file_path = '/Users/macbookair/Desktop/integrator project/Ecommerce_FAQ_Chatbot_dataset.json'
documents = load_data(file_path)
print(documents)
collection = init_chroma()
print(collection)
add_documents_to_chroma(collection, documents)
print("Documents added to ChromaDB collection.")
query = "How can I create an account?"
results = search_documents(collection, query, k=5)
response = generate_answer(query)
print ("Generated Answer:", response)