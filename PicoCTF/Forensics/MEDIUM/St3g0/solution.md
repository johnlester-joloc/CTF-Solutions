# PROBLEM

<img width="507" height="116" alt="image" src="https://github.com/user-attachments/assets/ac2d841a-e56a-4942-8903-1375d6bd7263" />

We are given a png file and no clues

<img width="585" height="172" alt="pico flag" src="https://github.com/user-attachments/assets/eb06633d-d0ab-4005-bbdf-d24d6e790964" />


# SOLUTION

Since this is a png file, we will use a basic LSB check using zsteg

          zsteg pico.flag.png

You should find the flag
