# PROBLEM

<img width="425" height="100" alt="image" src="https://github.com/user-attachments/assets/c24bee77-f13f-422c-93a1-b782a67b5f94" />

We are given a zip file. Open it to find an image inside

![ukn_reality](https://github.com/user-attachments/assets/a67c9e63-6488-47af-935d-77b7aa49e409)

# SOLUTION

This is a jpg file. jpg files don't have a lot of options for hiding the flag other than through the metadata

          exiftool ukn_reality.jpg

This is the output:

<img width="696" height="348" alt="image" src="https://github.com/user-attachments/assets/efc93b18-b444-4783-94c6-e81b36e328f8" />

There is a base64 text in the Attribution URL

          cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg==

Convert it to text

          echo cGljb0NURntNRTc0RDQ3QV9ISUREM05fM2I5MjA5YTJ9Cg== | base64 -d 

You should get the flag
