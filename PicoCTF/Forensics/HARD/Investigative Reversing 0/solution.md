<img width="657" height="260" alt="image" src="https://github.com/user-attachments/assets/10074461-8855-4155-a2f9-854f9f2f9892" /># PROBLEM

<img width="594" height="102" alt="image" src="https://github.com/user-attachments/assets/99080d20-2661-43bb-acdc-7976c305ba5e" />

# SOLUTION

First, we must understand what is happening inside our binary file. Use Ghidra to decompile it

<img width="813" height="434" alt="image" src="https://github.com/user-attachments/assets/211d6d83-f401-426b-bdf0-394de5556fa6" />

If you follow the steps, you should see something like this:

<img width="1919" height="1138" alt="image" src="https://github.com/user-attachments/assets/8a50e2a7-94b9-44fd-a638-cba01e5f3699" />

Open the search tab, select Program Text

<img width="323" height="504" alt="image" src="https://github.com/user-attachments/assets/29a8a2c6-e2cd-49b0-bac1-1e8c7aec6103" />

Select Functions and type main. This will search for the main function

<img width="495" height="543" alt="image" src="https://github.com/user-attachments/assets/804e46c6-fcc9-40e3-8d0d-8c9b6359431f" />

Click the code block to see the decompiled assembly

<img width="536" height="444" alt="image" src="https://github.com/user-attachments/assets/ab229c56-a18e-4b68-aeae-0f29d9cb2497" />

<img width="939" height="789" alt="image" src="https://github.com/user-attachments/assets/a8b1c50e-b052-4b49-a8a4-0634945eb3c7" />

We can now read the file as a C program. There are two things that I noticed.

1. Variable Declarations
<img width="193" height="255" alt="image" src="https://github.com/user-attachments/assets/ddb91638-7139-4a96-a637-25cf0694edf3" />

2. fopen invocations
<img width="657" height="260" alt="image" src="https://github.com/user-attachments/assets/3e2bda91-ca1f-417a-9096-01d4ec120f22" />

Notice that the program opened **flag.txt** in read mode as *_stream*. This is likely the source of our flag

<img width="331" height="28" alt="image" src="https://github.com/user-attachments/assets/eeb40351-3a2c-45e7-a037-69d7b38fcd57" />

It also opened our image, **mystery.png** in *append* mode as *_stream_00*. This means our flag was most likely appended to our image

PNG files have an IEND at the end of the data section, marking the end of the pixel data. Anything that comes after this will not be rendered, so you can technically append anything to PNG

To verify that something was appended to our PNG file, we will use xxd

          xxd mystery.png

<img width="569" height="68" alt="image" src="https://github.com/user-attachments/assets/1d7ec9fb-4098-4c61-b8e8-1330a634788a" />

After the IEND, we found this text

          picoCTK.k5zsid6q_f0a9b767}

This *looks* like our flag but it is not our flag just yet. Let us investigate the binary file more

<img width="375" height="24" alt="image" src="https://github.com/user-attachments/assets/d7dd4bdd-656b-4752-ab99-2ddbe088e6a2" />

The file contents of **flag.txt** was stored inside a char array called *local_38*

<img width="373" height="24" alt="image" src="https://github.com/user-attachments/assets/5b4f2000-74b0-444a-ab05-b4662aee6697" />

Then, the first 4 characters of the flag was appended

<img width="344" height="91" alt="image" src="https://github.com/user-attachments/assets/f8ae25a6-6ef1-466c-bc98-57034db5db0f" />

Two uninitialized variables, most likely containing garbage value, was appended for the 5th and 6th characters

<img width="318" height="43" alt="image" src="https://github.com/user-attachments/assets/f841e8be-4f37-4d56-ab86-4ac21a042abb" />

A for loop is responsible for 7th to 15th character, but with an offset of 5

<img width="583" height="68" alt="image" src="https://github.com/user-attachments/assets/0b5b720f-683c-48ef-9ca9-c027acebb26e" />

Another uninitialized variable is used for the 16th character with negative offset of 3

<img width="464" height="23" alt="image" src="https://github.com/user-attachments/assets/626c2c93-3ff1-4f04-8c7b-19a7c0103cde" />

The rest are appended as is

<img width="597" height="72" alt="image" src="https://github.com/user-attachments/assets/fc8a3ac8-12d1-4925-8a68-2fe5b72e12cc" />

Now it is just a matter of decoding the text based on the clues. Let's make a simple python script for this (file is in the solution directory)

<img width="456" height="322" alt="image" src="https://github.com/user-attachments/assets/ef6e9bc0-22a7-4a80-893f-3fb23eac18a2" />

Then swap '(' to '{' to follow the picoCTF format, and there's your flag

