import openai
import sqlite3
import pickle

'''
Creates embeddings for the chuncks of text using OpenAI's text embedding model. 
Connects to the SQLite database and stores the embeddings in a table.

Parameters:
chunks - a list of strings to be embedded
table_name - the name of the table to store the embeddings

Returns: None
'''
def create_embeddings(chunks, model="text-embedding-3-small"):

    # Connect to the database
    conn = sqlite3.connect('coxswain_rag.db')
    c = conn.cursor()

    # Create embeddings for each chunk
    client = openai.Client()
    embeddings = []

    for chunk in chunks:
        result = (client.embeddings.create(input=chunk, model=model)).data[0].embedding
        result_pickle = pickle.dumps(result)
        
        # Store the embeddings in the database
        c.execute("UPDATE chunks SET embeddings = ? WHERE chunk = ?", (sqlite3.Binary(result_pickle), chunk))
        conn.commit()
    
    # Close the database connection
    conn.close()