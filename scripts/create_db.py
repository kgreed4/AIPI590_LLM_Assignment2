import sqlite3

'''
Set up SQlite database to store the chunks and their corresponding document names
'''
def create_db():
    conn = sqlite3.connect('coxswain_rag.db')
    c = conn.cursor()
    
    # Drop the 'chunks' table if it exists
    c.execute("DROP TABLE IF EXISTS chunks")

    c.execute('''CREATE TABLE IF NOT EXISTS chunks (
              id INTEGER PRIMARY KEY, doc_name TEXT, chunk TEXT, embeddings BLOB, cosine_simiarlity FLOAT
              )''')
    conn.commit()
    conn.close()