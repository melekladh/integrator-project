def generate_answer(question):
    from llama_cpp import Llama

    # chemin vers le fichier .bin ggml
    model_path = "/Users/macbookair/Desktop/integrator project/dolphin-2.6-mistral-7b.Q2_K.gguf"

    llm = Llama(model_path=model_path)

    # Génération simple

    output = llm(question, max_tokens=200)
    print(output)
    return output
