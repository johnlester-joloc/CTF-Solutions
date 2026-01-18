# PROBLEM

<img width="613" height="381" alt="image" src="https://github.com/user-attachments/assets/3b43ecc9-f1eb-4791-bebc-bfa58461860c" />

We are given a txt file. Opening it reveals this mess:

<img width="873" height="702" alt="image" src="https://github.com/user-attachments/assets/e3ba5144-a871-4101-998b-a0f3c0f770f9" />

# SOLUTION

First thing I notice is that this is in base64. Let's try converting it to see what's up, but because the file is so big, it's smarter to just pass the base64 result to a new file

          cat logs.txt | base64 -d > b64.txt

Now if we try to open it, we get this:

<img width="1465" height="414" alt="image" src="https://github.com/user-attachments/assets/5aa3f5ee-0048-4c9f-8ceb-d25f1fe46e6d" />

The first few bytes spell out 'PNG'. Files store their file type in the header bytes, also known as the magic bytes. It tells the computer how to open the file.
Since we know that this is a PNG, all we need to do is to convert it from a .txt to a .png

          cp b64.txt pic.png

<img width="896" height="1152" alt="image" src="https://github.com/user-attachments/assets/9f24d058-0441-4aef-9c94-e72d396ff1e7" />

There's a series of characters at the bottom of the picture. If you look carefully, it contains only hex characters, so this is clearly in hex

          7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F62396163346362397D

We can convert hex using this command

          echo "7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F62396163346362397D" | xxd -r -p

Now we have the flag!
