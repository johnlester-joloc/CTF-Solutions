# PROBLEM

<img width="623" height="203" alt="image" src="https://github.com/user-attachments/assets/84cc81c4-8e7a-4c35-9002-0c2726880fab" />

We are given a broken file. You cannot open it. It also tells us that "maybe a couple of bytes could make all the difference".

# SOLUTION

This is a classic case of a broken file header. Let's check the header bytes to verify. I will be using xxd

<img width="557" height="193" alt="image" src="https://github.com/user-attachments/assets/346247ac-291c-4144-b3a6-e0fbd93a254c" />

It says that it is a JFIF. JFIF header is an image file (a JPEG File Interchangeble Format), so we can expect that this is a picture. Let's check if the bytes themselves are correct.

**EXPECTED BYTES**

          FF D8 FF E0

**ACTUAL BYTES**

          5C 78 FF E0

The actual bytes do not match the expected bytes. We must change the actual bytes to the expected bytes. There are many ways to do this, but the most convenient method is using hexedit

          hexedit file

You can study the controls for this tool. Our goal now is to fix the bytes. Simply type the expected bytes to replace the actual bytes

We can now see that the header bytes are correct

<img width="564" height="196" alt="image" src="https://github.com/user-attachments/assets/fcda4c75-fff5-4ba1-9d03-500c3c681d99" />

Last step is to convert the file to a jpg

          cp file file.jpg

And we get the flag


