# PROBLEM

<img width="574" height="120" alt="image" src="https://github.com/user-attachments/assets/2b6e29b6-cb42-4116-b7b7-dc13b9a7edd8" />

We are given an image file. 

# SOLUTION

Let's check the metadata using exiftool

          exiftool red.png

<img width="1465" height="409" alt="image" src="https://github.com/user-attachments/assets/8575fbfe-d517-4875-9e2d-593a79587389" />

There's a poem here.

  ``Crimson heart, vibrant and bold,.
  Hearts flutter at your sight..
  Evenings glow softly red,.
  Cherries burst with sweet life..
  Kisses linger with your warmth..
  Love deep as merlot..
  Scarlet leaves falling softly,.Bold in every stroke``

If you look closely at the poem, the first letter of each line (capitalized) spell out as:

          CHECK LSB

LSB stands for Least Significant Bit. In a byte, the right-most bit is the LSB. This is because when it is flipped, it adds (or subtracts) only 1 to the value of the byte in decimal.
Image files contain color channels. For PNG, RGBA is the most common. Typically, there is one byte assigned per color channel (total of 32 bytes per pixel). You can embed
information inside an image file by simply scattering the bits of the information to the LSB of the image, resulting in very minimal change to the color of each pixel.

We can extract the LSB of an image using zsteg

          zsteg red.png

<img width="1461" height="275" alt="image" src="https://github.com/user-attachments/assets/747ab9a1-0fe0-4133-a909-eae179346133" />

There are two extracted text, one is the poem, the other is a base64 string. The extracted files here don't matter since that is a common result of zsteg (not every LSB is used, but zsteg stil parses all of them)

``cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==``

Notice that there are repeated "==" here. Base64 string always ends with "==", so this means it is actually repeated. We only care about the text before the first "==" including the "==" itself.

``cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ==``

Decode it using base64

          echo cGljb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVffQ== | base64 -d

And you get the flag

