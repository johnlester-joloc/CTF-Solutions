<img width="480" height="31" alt="image" src="https://github.com/user-attachments/assets/b01286eb-5880-41da-99ff-a041e383016a" /># PROBLEM

<img width="610" height="179" alt="image" src="https://github.com/user-attachments/assets/7febf83b-471c-4ecd-ba8f-4c7eabc5b665" />

We are given an image file. Opening it gives us this

![img](https://github.com/user-attachments/assets/fee7d5a8-b1ff-4cb1-a168-935f5a37330e)

Just a random image of a screen.

# SOLUTION

I checked the metadata using exiftool

          exiftool img.jpg

<img width="690" height="449" alt="image" src="https://github.com/user-attachments/assets/949e0ad0-467d-4924-a462-439c9ec650b9" />

We have a suspicious comment tag

          Comment: c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9

This is encoded using base64. Decode it using base64

          echo c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9 | base64 -d

We get this

          steghide:cEF6endvcmQ=

Steghide is a popular steganography tool. It can lock files with a password. Clearly this tells us to open the file using steghide with the password we just discovered.

          steghide extract -sf img.jpg -p cEF6endvcmQ=

*extract -> tells steghide to extract*
*-sf -> specifies the file*

*img.jpg -> the file to extract*

*-p -> specifies the passphrase*

*cEF6endvcmQ= -> the passphrase*

We unfortunately get this result:

<img width="480" height="31" alt="image" src="https://github.com/user-attachments/assets/b04d630d-adbd-4d40-9bd4-1fe03f1f1c20" />

Looking closely at the passphrase, we can see that it is also base65 (trailing '=' symbol). Let's try decoding it

          echo cEF6endvcmQ= | base64 -d

We get this

<img width="139" height="22" alt="image" src="https://github.com/user-attachments/assets/ee73789d-32f1-4350-b961-65f157af97c7" />

Let's try steghide again

          steghide extract -sf img.jpg -p pAzzword

It gave us a file called 'flag.txt'

Opening it reveals the flag 

<details align="center"><summary>CLICK TO REVEAL THE FLAG</summary>picoCTF{h1dd3n_1n_1m4g3_5d4cba73}</details>


