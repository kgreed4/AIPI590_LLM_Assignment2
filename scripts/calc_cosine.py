import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

import sqlite3
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

'''
Semantic search the embeddings using cosine similarity to locate the most similar chunk given a query.
'''
def calculate_and_store_cosine_similarity(query_embedding):
    # Connect to the SQLite database
    conn = sqlite3.connect('coxswain_rag.db')
    cursor = conn.cursor()

    # Fetch all embeddings from the database
    cursor.execute("SELECT chunk, embeddings FROM chunks WHERE embeddings IS NOT NULL")
    rows = cursor.fetchall()

    # Calculate cosine similarity for each embedding
    similarities = []
    for row in rows:
        chunk, embedding_pickle = row
        # Convert binary data back to numpy array
        embedding = pickle.loads(embedding_pickle)
        # Calculate cosine similarity
        similarity_score = cosine_similarity([query_embedding], [embedding])[0][0]
        similarities.append((chunk, similarity_score))

    # Store the similarity scores in the database
    for chunk, similarity_score in similarities:
        cursor.execute("UPDATE chunks SET cosine_simiarlity = ? WHERE chunk = ?", (similarity_score, chunk))
    conn.commit()

    # Get the top 3 similarity scores
    top_similarities = sorted(similarities, key=lambda x: x[1], reverse=True)[:5]

    # Close cursor and connection
    cursor.close()
    conn.close()

    return top_similarities