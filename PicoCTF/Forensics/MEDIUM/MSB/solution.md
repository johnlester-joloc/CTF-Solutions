# PROBLEM

<img width="619" height="181" alt="image" src="https://github.com/user-attachments/assets/3cc4883f-07ac-4fca-84c2-431c460791e2" />

We are given this image.

<img width="1074" height="1500" alt="pic" src="https://github.com/user-attachments/assets/c02927dd-d075-43ed-932b-48e0a5d15417" />

We must somehow find the flag in this image

# SOLUTION

The title of the problem is MSB. This stands for Most Significant Bit. 1 byte is 8 bits, and the MSB of 1 byte

          1 0 0 0 0 0 0 0

would be the left-most bit (the 1).

Most steganography challenges that involve images uses the Least Significant Bit (LSB), but we need the MSB. We can't use our usual tools here. 
Instead, we use online tools

Visit [StegoOnline](https://georgeom.net/StegOnline/extract)

<img width="1011" height="584" alt="image" src="https://github.com/user-attachments/assets/8928572c-838c-4a46-a6be-5811d9eb4d71" />

Drag and drop your image. You should see these options

<img width="1014" height="666" alt="image" src="https://github.com/user-attachments/assets/d8e40f23-903e-49b2-bc36-b54c32497e8f" />

Select **Extract Files/Data**

<img width="1017" height="843" alt="image" src="https://github.com/user-attachments/assets/5932c0ca-7f02-4729-b3a6-0d8829279eaa" />

Since we are looking for the MSB, tick the box at row 7

<img width="1026" height="858" alt="image" src="https://github.com/user-attachments/assets/7b50da95-007b-4311-b3fb-45f83395f704" />

<img width="991" height="565" alt="image" src="https://github.com/user-attachments/assets/cf3ceb08-c812-4d47-9d31-8a1da8f673d3" />

Downlaod the extracted data

You will get a text file containing a large amount of text. Use grep to filter the flag

          cat pic.dat | grep "picoCTF"

And there's your flag
