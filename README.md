# Rowing (& Coxswain) RAG
For AIPI 590: Large Language Models, Assignment 2, a Retrieval Augmented Generation system was created for those who need a little more rowing in their life! The system focuses on improving knowledge about rowing in general, but also specifically for coxswains. A typcial rowing shell has 8 seats, one for each rower, however, the 9th seat is reserved for the often overlooked, but essential role of the coxswain. This RAG is meant for all the 9th seats out there! A one stop shop for all of your rowing, coxing, and leadership needs.

## Data
The data contains coxswain references collected from a variety of coaches and levels--from novice, collegiate, to Olympic. Additionally, the data contains the 2023 USRowing Rules of Rowing and the NCAA Rowing Championships Manual. 

## Creation
The RAG is implemented using a chunk size of 500 with provisons to ensure sentences and paragraphs are kept together. The chunks are then passed into an SQLite database and stored before being embedded by the OpenAI embedding API. The query asked by the user is also embedded in this same space. Next, the cosine similarity is calculated between the query and the chunks of data stored. The top 5 cosine similarity scores are then given to the LLM to construct a response. Finally, the response is populated to the user.

## Comparison
The RAG out-performed the LLM, GPT-3.5 turbo, in 81.8% of cases. These (11) test questions were generated based on what a typical coxswain may inquire about, ranging in experience from a novice to a seasoned coxswain. 

The test questions and answers are as follows (which can also be found in `testQuestions.txt`:

Questions:
1. How does a quick start work?
2. What are common coxswain calls?
3. How do I enter a stake boat?
4. What are the top 3 priorities of a coxswain?
5. How does the steering rudder in an eight work?
6. At the catch, how should a rower’s blade enter the water? What can a coxswain say to help the rower get the blade in quick and sharp at the front end?
7. How do starting commands with lights work?
8. What is a bow ball?
9. As a coxswain, how do I protest after a race?
10. What is a ratio call?
11. What is a cox box?

Answers:
1. The starter announces “this will be quick start,” there is no polling of the crews. The starter then raises the flag and says, “This is a quick start. Attention, go!”
2. Common coxswain calls include things about rhythm, technique, and positioning against over crews/on the course. For example, these may include, “legs”, “jump”, “push”, “Katie, you’re skying your blade. Raise your hands at the catch and lock in.”, “We are a seat up”, “Two seats down”, “Got open water on lane 2”. 
3. Enter a stake boat by rowing parallel to it and then spinning into your lane. Back into the stake boat slowly. Have the rowers in bow, 2 seat, and 3 seat scull the blades to adjust your point.
4. Top three priorities of a coxswain are safety, practice/race management, and motivation. 
5. Steering a rudder in an eight works by pushing the steering cable (string) forward on the side in which you want to go (have your bow point). For example, if you want to go to port, the left, slide your left hand forward while holding the steering cable. 
6. A rower’s blade should enter the water completely squared when they are not full extension. It should enter the water quickly and sharply, there is no hesitation. A coxswain can say “quick”, “in”, “up” with a sharp tone of voice to help a rower get her blade in quickly.
7. The announcer will announce `Attention!` and the lights will change from neutral to red. Then, after a distinct variable pause, the light will change from red to green and an audible noise will sound.
8. Every boat has a white shiny plastic ball on the bow. It has to be firmly mounted. It is to protect the boat and the rowers from injury. 
9. Once an objection is lodged, a Crew wishing to be heard before the Jury shall submit a concise written statement. The protest must be started on the water by the coxswain raising her hand at the end of the race. The protest must have solution for the change that they have proposed. 
10. It is a call to shift the tone of the stroke. The goal of this call is to get longer on the recovery and faster on the drive. `Slide goes down, power with leg drive goes up.
11. A speaker tool that connects to the boat and allows the coxswain's voice to be heard through a microphone. It also has a stroke rate monitor and a timer. 


<img width="629" alt="Screenshot 2024-02-20 at 9 41 02 PM" src="https://github.com/kgreed4/AIPI590_LLM_Assignment2/assets/75132518/8b5512f9-4d9a-4b3d-9472-84dbd080c90f">

