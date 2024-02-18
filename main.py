from scripts.embed_query import embed_query
from scripts.calc_cosine import calculate_and_store_cosine_similarity
from scripts.connect_to_LLM import connect_to_LLM

def main(query):
    query_embedding = embed_query(query)
    top_similarity_scores = calculate_and_store_cosine_similarity(query_embedding)
    response = connect_to_LLM(query, top_similarity_scores)
    return response
