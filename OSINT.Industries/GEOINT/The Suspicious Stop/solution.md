# PROBLEM

Rules
Passive OSINT only
No interaction with people, places, or accounts
No authentication or recovery attempts
Reasoning and analysis only
Scenario
A small boat departing from Marseille follows the same route to the same destination every day. However, on one particular day, it unexpectedly deviated from its usual itinerary and stopped at a specific location.

We suspect this unusual detour is connected to black-market activity. Intelligence indicates that the boat's owner met with an individual who arrived on a bike, and the two then entered a nearby restaurant together.

Starting Material
Provided GPS logs: coordinates.nmea
Challenge Objective
Your task is to identify :

The restaurant's name where they met.
Its full address.
Flag submission
Submit the flag using the following format:

OSINT{Name_Address}

Note: Remove "Restaurant", only provide its name.

Example (not the answer):
OSINT{Le_Colimaçon_44_Rue_Vieille_du_Temple,_75004_Paris}

# SOLUTION

The problem involves a `.nmea` file, which is a text file containing timestamped GPS coordinates typically used for tracking. This file can be loaded into a map
through (nmeagen.org)[nmeagen.org] 

<img width="300" height="506" alt="image" src="https://github.com/user-attachments/assets/0397a54a-c020-4c4a-8935-964b66796c44" />

Based on the map, we can see the mentioned deviation. Zooming in reveals the exact location where the boat stopped

<img width="895" height="445" alt="image" src="https://github.com/user-attachments/assets/2b91e2f9-2198-4009-ae11-609339abb512" />

There is a restaurant nearby named **Les Tamaris**, which could be the right restaurant. Cross-referencing with Google Maps reveal that the next
closest restaurant is too far to be reasonable. Google Map also tells us the exact address of Les Tamaris

<img width="508" height="241" alt="image" src="https://github.com/user-attachments/assets/dd9fbdb5-7ea3-44f4-9c43-a4ea8bb9a31c" />

Plugging the restaurant name and address to the flag format gives you the correct flag
