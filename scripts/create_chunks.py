'''Create chunks of text that can be processed and vectorized.
Want the chunks to end at the end of a senetence and the end of a paragraph.

Parameters: 
text - a string to be chunked 
Returns: a list of chunks of text
'''
def create_chunks(text, doc_name, chunk_size=500):
    # Initialize variables
    chunks = []
    current_chunk = ''
    current_size = 0
    
    # Split the text into paragraphs
    paragraphs = text.split('\n\n')

    # Iterate through each paragraph
    for paragraph in paragraphs:
        # Split the paragraph into sentences
        sentences = paragraph.split('. ')
        
        # Iterate through each sentence
        for sentence in sentences:
            # Check if adding the sentence to the current chunk would exceed the chunk size
            if len(current_chunk) + len(sentence) + 2 <= chunk_size:  # Add 2 for the period and space
                # Add the sentence to the current chunk
                if current_chunk:
                    current_chunk += '. ' + sentence
                else:
                    current_chunk += sentence
                current_size += len(sentence) + 2  # Update the current size
            else:
                # Add the current chunk to the list of chunks
                chunks.append(current_chunk)
                # Reset the current chunk and size to start a new chunk
                current_chunk = sentence
                current_size = len(sentence)
        
        # Add the last chunk of the paragraph
        if current_chunk:
            chunks.append(current_chunk)
            current_chunk = ''
            current_size = 0
    
    # Return the list of chunks
    print(f'Created {len(chunks)} chunks')

    # Add the chunks to the database
    conn = sqlite3.connect('coxswain_rag.db')
    c = conn.cursor()
    for chunk in chunks:
        c.execute('INSERT INTO chunks (doc_name, chunk) VALUES (?, ?)', (doc_name, chunk))
    conn.commit()
    conn.close()

    return chunks