import openai

def embed_query(query, model="text-embedding-3-small"):
    # Create an embedding for the query
    client = openai.Client()
    result = client.embeddings.create(input=query, model=model)
    return result.data[0].embedding