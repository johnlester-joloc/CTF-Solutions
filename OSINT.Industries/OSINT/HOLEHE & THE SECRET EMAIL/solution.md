# PROBLEM
---
You are investigating the origins of a popular OSINT tool used to pivot from email addresses to online accounts: Holehe.

Behind every tool, there is a creator — and behind that creator, there is an email address.

Your mission is to trace back the very first appearance of the creator’s email address online and determine the exact date it was created.

Objective
Using open-source intelligence only, find:

The creator of Holehe
The public email address used for Holehe
The exact creation date of this email address
The final flag must be based only on this date.

Flag Format
OSINT{DD-MM-YYYY}

Example (not the real answer):
OSINT{01-01-2020}

Rules
Use only legal, open-source information
Do not contact the developer
No exploitation, intrusion, OSINT only
Everything can be found through:
Code repositories
Public profiles
Archives
Lawful OSINT sources

# SOLUTION

I first searched for the Holehe Website and visited the About page and Contact page and found nothing there. Instead, I visited
the Holehe Github repo and identified the creator

<img width="1177" height="743" alt="image" src="https://github.com/user-attachments/assets/45a14e78-9026-4b9e-a767-9b07cba2ff07" />

<img width="451" height="937" alt="image" src="https://github.com/user-attachments/assets/fc5cfb3d-acae-49fb-98a4-12bc565cbe81" />

The website creator is _megadose_ and their email is `megadose@protonmail.com`. Since the flag involves the email creation, we need to
identify the creation date. I used [this](https://kriztalz.sh/proton-date/) website.

<img width="577" height="370" alt="image" src="https://github.com/user-attachments/assets/ef766c7f-d512-482c-a4ac-4bcedad18d77" />

Plugging in the creation date gives you the flag
