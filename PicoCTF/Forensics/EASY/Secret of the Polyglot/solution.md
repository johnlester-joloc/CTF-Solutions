# PROBLEM

<img width="617" height="295" alt="image" src="https://github.com/user-attachments/assets/19601b8f-ed53-4d60-83c5-cd741a1e091d" />

We are given a pdf file. Opening gives us half of the flag

<img width="1003" height="749" alt="image" src="https://github.com/user-attachments/assets/685a2758-113c-40e7-a7d9-b988c8ee5746" />

We must now find the other half

# SOLUTION

First let us dump the contents of this file

          cat flag2of2-final.pdf

This is the result:

<img width="1522" height="259" alt="image" src="https://github.com/user-attachments/assets/14d4390a-00de-450c-a87c-0b49673d6468" />

It's quite big so I will only show this part. We can see the PNG header. Let's try converting the file to a png

          cp flag2of2-final.pdf a.png

You shoul get an image that contains the other half of the flag
