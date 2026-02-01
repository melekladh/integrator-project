import json

def load_data(file_path):

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    documents = []
    for item in data["questions"]:
        doc = f"Question: {item['question']}\nReponse: {item['answer']}"
        documents.append(doc)

    return documents



 

