# PROBLEM

<img width="584" height="183" alt="image" src="https://github.com/user-attachments/assets/53fb81d7-8167-4f18-bc70-08169995febe" />

We are given an image file

<img width="512" height="504" alt="image" src="https://github.com/user-attachments/assets/db093e8e-2f02-4e24-af17-3756ccbcf0ef" />

# SOLUTION

Let us use zsteg since this is a png

          zsteg flag.png

We found trailing data at the end of the IEND chunk, specifically a zip file

<img width="1373" height="342" alt="image" src="https://github.com/user-attachments/assets/5c6c091a-1eb6-49f5-95f3-9fecefb3c73a" />

Let's verify this using binwalk

          binwalk flag.png

It seems that it is indeed a zip file, with a folder named "secret" and a file called flag.png

<img width="1168" height="156" alt="image" src="https://github.com/user-attachments/assets/d7107deb-29ed-4dda-872a-f73ff8d83635" />

We can extract this using biwnalk

        binwalk -e flag.png

This will generate a folder containing the extracted file

<img width="156" height="187" alt="image" src="https://github.com/user-attachments/assets/e1f370e9-b722-4dcd-978b-293f6d238b15" />

Open the secret folder and you will find an image containing the flag
