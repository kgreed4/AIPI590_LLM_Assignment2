import openai

'''
Connect to the LLM and generate a response to a query using the top 3 most similar chunks.

Parameters:
query - a string query
top_similarities - a list of tuples containing the most similar chunks and their similarity scores

Returns: a string response
'''
def connect_to_LLM(query, top_similarities):
    # Prompt gpt-3.5 to generate a response
    client = openai.Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": f"Using the top 3 most similar chunks {top_similarities}, please generate a response to the query: {query}. If none of them are relevant, please say `I don't know`."
            }
        ])
    return response.choices[0].message.content