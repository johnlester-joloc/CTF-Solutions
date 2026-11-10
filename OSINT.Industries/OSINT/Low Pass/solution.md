# PROBLEM

Rules
Passive OSINT only
No interaction with people, places, or accounts
No authentication or recovery attempts
Reasoning and analysis only
Scenario
A short video has been shared publicly online showing a series of helicopters flying at low altitude over a rural area in France. Analyze all publicly available information and determine in which municipality the helicopters were flying, as well as the official helicopter model name of the first helicopyer.

Starting Material
helicopter.mp4
Challenge Objective
Your task is to identify :

The name of the municipality in which the helicopters were flying.
The official helicopter model name.
Flag submission
Submit the flag using the following format:
OSINT{municipality_model}

Example (not the answer):
OSINT{Saint-Dié-en-Vosges_AS532_Cougar}

# SOLUTION

The problem involves a video of two helicopters performing a low pass flyby on a farming field in France. Upon inspection, I saw a frame where the bottom view of
the helicopter is most visible

<img width="635" height="1140" alt="Screenshot 2026-11-11 013028" src="https://github.com/user-attachments/assets/bf59b4b7-3979-4418-bb6a-4a3acf9c5ab8" />

Plugging this screenshot to Google Lens gave me this Instagram post containing this exact video

<img width="1223" height="1017" alt="image" src="https://github.com/user-attachments/assets/6b9ef185-4d6c-4119-ba71-a0f4064fb1bb" />

As you can see, the location is tagged at the bottom

<img width="382" height="175" alt="image" src="https://github.com/user-attachments/assets/3b93fa75-a5e9-463a-ba9f-0431159eb84b" />

Châlons-sur-Marne was renamed to Châlons-en-Champagne in 1997, meaning we have two possible municipal names.

Also, the tagged account `@@aviationlegere2larmee2terre` is the official Instagram account of ALAT, the French Army Light Aviation. Based on Wikipedia
ALAT uses both Eurocopter Cougar and Eurocopter Tiger. The provided picture in Wikipedia for the Eurocopter Tiger matches the same helicopter from the video,
both having the same amount of blades, landing gear, and camo

<img width="732" height="549" alt="image" src="https://github.com/user-attachments/assets/332cfd24-58cf-43d8-8570-b93f151862b9" />

Based on the ALAT Wikipedia, it is the EC665 Tiger. The EC665 Tiger has many variants. We can see the helicopter's side profile in another frame

<img width="450" height="281" alt="image" src="https://github.com/user-attachments/assets/cb7600f3-6d95-4722-b7a5-3da3795ea7fb" />

I noticed the the model name can sometimes be spelled as `Tigre`. Trying this variation gave me the correct answer
