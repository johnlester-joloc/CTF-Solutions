# PROBLEM

<img width="454" height="150" alt="image" src="https://github.com/user-attachments/assets/bcf11d3a-2821-4b92-bdfa-c475b2d1f1f2" />

We are given an SVG image. These are typically xml files used for graphics, popular in frontend development

<img width="1196" height="1034" alt="image" src="https://github.com/user-attachments/assets/e433eda2-4cc8-4882-99c3-bb47b2306eb5" />

# SOLUTION

If you open the svg file, it will take you to your browser. Since we know that this is an SVG, the flag is most likely within the xml stuff

Right click on the image and select Inspect

<img width="473" height="451" alt="image" src="https://github.com/user-attachments/assets/442ab79d-d52b-4591-825f-d03c82fd354e" />

This should pop up a section in your browser where you can view the xml elements

<img width="698" height="527" alt="image" src="https://github.com/user-attachments/assets/a503ff51-d6b0-4b63-b873-6cb8818f8762" />

There's a very sus element here

<img width="675" height="95" alt="image" src="https://github.com/user-attachments/assets/9e75a713-9af5-4973-8b06-61bbca795479" />

And it highlights some microscopic text

<img width="1201" height="1037" alt="image" src="https://github.com/user-attachments/assets/1113732d-bd89-46d5-89d0-0bf942aa9113" />

Unfortunately for me, I don't own an 8k monitor, and neither do you, so there's no chance we can just zoom in. Instead, let's expand the text element

<img width="697" height="269" alt="image" src="https://github.com/user-attachments/assets/d2397fa9-4f9e-4bcd-b539-98f7be2ee62b" />

There's a <tspan> tag inside. I don't really know what that is, but it encloses our flag. 

<img width="689" height="424" alt="image" src="https://github.com/user-attachments/assets/3fa1699a-1c0f-4e94-baa0-a40f9d0ef614" />

Just type it out and there's your flag!
