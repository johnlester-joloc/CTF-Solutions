# PROBLEM

<img width="623" height="261" alt="image" src="https://github.com/user-attachments/assets/b7158140-05d7-487a-bd63-da9ce30a22cc" />

We are given some file and not much instruction.

# SOLUTION

I xxd to check what kind of file it is

          xxd advanced-potion-making | head

<img width="568" height="196" alt="image" src="https://github.com/user-attachments/assets/ad239403-11b7-41c0-a0ec-be03f5b5af33" />

Based on the output, we can infer that this is a corrupted PNG file. Let's fix it using hexedit

          hexedit advanced-potion-making

<img width="968" height="678" alt="image" src="https://github.com/user-attachments/assets/afa8e7bb-5a3a-46f3-a7d4-c9c57ba87408" />

The head bytes are all wrong. It should be like this

          89 50 4E 47 0D 0A 1A 0A

The IHDR chunk is also wrong. It should be all 0s and 0D before 49

<img width="309" height="25" alt="image" src="https://github.com/user-attachments/assets/3446caae-fb0e-4a2c-85fd-972283db453a" />

          00 00 00 0D 49 48 44 52

After fixing that, all we get is this

<img width="1428" height="815" alt="image" src="https://github.com/user-attachments/assets/506ded3f-08e5-4538-9dd0-ab7a214b0830" />

It's just red everywhere. I tried extracting the channels and it led me to nowhere. Eventually, I tried to convert it to black and white. Most sites didn't work as intended until i found this:

[Online Image Editor](online-image-editor.com)

Change it to B&W and you'll get the flag


