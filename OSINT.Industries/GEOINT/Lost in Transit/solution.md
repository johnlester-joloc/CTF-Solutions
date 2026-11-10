# PROBLEM

Hello,

a photo was taken, apparently in a train station.

Your mission is to determine:

1. **Which train station** this photo was taken in  
2. **The approximate time window** when it was taken, with a precision of **two hours**

Expected time format:  
- 8am–10am  
- 10am–12pm  
- 12pm–2pm  
- 2pm–4pm  
- etc.

---

### 🎯 Flag format  
`OSINT{station_name_time-range}`

<img width="1320" height="1562" alt="img" src="https://github.com/user-attachments/assets/7031b9a8-6ab2-4986-80e0-02fa36c12b99" />

# SOLUTION

Checking the surroundings, I immediately noticed a French flag on top of the main building. This tells us that we are in France

<img width="352" height="372" alt="image" src="https://github.com/user-attachments/assets/a6dc22b8-dc40-4de1-8da6-4192e3771d4d" />

Using Google Lens on the main building with the French Flag, I found a visual match with a stock photo with the St. Charles station in Marsaille, France
<img width="1137" height="792" alt="image" src="https://github.com/user-attachments/assets/3631f138-ae43-440d-841c-1a4464c1b0d9" />

After identifying the station, the next task was to identify the approximate time. I noticed the shadow cast by tourists to be pointing towards the tracks
next to the main building

<img width="1320" height="1562" alt="imgs" src="https://github.com/user-attachments/assets/5a139c52-3797-4649-94ca-c130d4a48d1d" />

Next, I took a screenshot of the satellite view of the St. Charles station to compare the shadow angles.

<img width="732" height="418" alt="Screenshot 2026-11-11 014727" src="https://github.com/user-attachments/assets/2bd4206c-9d06-462e-b1d6-4a2af677f0a6" />

The blue line indicates the shadow angle, while the red dot indicates the approximate camera origin. Based on the shadow, the sun must be on the eastern side,
meaning it is currently day time. Likewise, the color of the sunlight is bright white and the shadow length is short, indicating that it must be close to noon.
This means the approximate time is 10am-12pm

Combining the station name and the approximate time gives you the correct flag

