# PROBLEM

<img width="605" height="304" alt="Screenshot 2026-01-16 234410" src="https://github.com/user-attachments/assets/015a0b1a-febe-4391-b281-04ecad23a6fd" />

We are given a suspicious pdf file. 

<img width="1014" height="956" alt="image" src="https://github.com/user-attachments/assets/a72e645b-3cd7-408a-bf98-8e5ecd61dcb8" />

## BLACKBARS
There are black bars present. We all know that the Federal Government tried to do this with the epstein files but we can EASILY retrieve what is hidden by just selecting it.

Pasting it gives us this:

**First Black Bar**

  				The author have done a great and good job

**Second Black Bar**

				  No flag here. Nice try though!

Of course it won't be that easy.

## EXIFTOOL
My next plan is to use exiftool. Exiftool allows you to dump the metadata inside a file.

					exiftool confidential.pdf

This gives us this result:

<img width="1161" height="541" alt="Screenshot 2026-01-16 235234" src="https://github.com/user-attachments/assets/e261b536-86f2-4ce9-a853-4c9bd8f501c6" />

If you look closely, there's a suspicious author section with an obvious base64 encoding.

					Author: cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOTk5ZTJhNH0=

We can decode this using base64 

					echo cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOTk5ZTJhNH0= | base64 -d

This gives us the flag

					picoCTF{puzzl3d_m3tadata_f0und!_c999e2a4}





