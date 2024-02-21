# Rowing (& Coxswain) RAG
For AIPI 590: Large Language Models, Assignment 2, a Retrieval Augmented Generation system was created for those who need a little more rowing in their life! The system focuses on improving knowledge about rowing in general, but also specifically for coxswains. A typcial rowing shell has 8 seats, one for each rower, however, the 9th seat is reserved for the often overlooked, but essential role of the coxswain. This RAG is meant for all the 9th seats out there! A one stop shop for all of your rowing, coxing, and leadership needs.

## Data
The data contains coxswain references collected from a variety of coaches and levels--from novice, collegiate, to Olympic. Additionally, the data contains the 2023 USRowing Rules of Rowing and the NCAA Rowing Championships Manual. 

## Creation
The RAG is implemented using a chunk size of 500 with provisons to ensure sentences and paragraphs are kept together. The chunks are then passed into an SQLite database and stored before being embedded by the OpenAI embedding API. The query asked by the user is also embedded in this same space. Next, the cosine similarity is calculated between the query and the chunks of data stored. The top 5 cosine similarity scores are then given to the LLM to construct a response. Finally, the response is populated to the user.

## Comparison
The RAG out-performed the LLM, GPT-3.5 turbo, in 81.8% of cases. These (11) test questions were generated based on what a typical coxswain may inquire about, ranging in experience from a novice to a seasoned coxswain. 
<img width="629" alt="Screenshot 2024-02-20 at 9 41 02 PM" src="https://github.com/kgreed4/AIPI590_LLM_Assignment2/assets/75132518/8b5512f9-4d9a-4b3d-9472-84dbd080c90f">

