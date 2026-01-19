# PROBLEM

<img width="469" height="129" alt="image" src="https://github.com/user-attachments/assets/d168e686-6767-4a6d-a7e8-b9a58723f820" />

We are given a disk image. Disk images are a snapshot of a disk (or drive). It's like a screenshot of the entire filesystem. 

# SOLUTION

We can try to mount the disk image, but I wouldn't do that first. I checked the hints and it says to use strings. For cases like this, it is better to start with general
forensic solutions first before mounting the image, because mounting (and partitioning) can take hours if the file is massive. 

Let's run strings on the file

          strings disko-1.dd

As expected, it gave us ALL of the strings inside the directory. I'm not even gonna bother taking a screenshot of that. What we need is a filter using grep.
We already know that the flag follows a format, so just use that as our filter

          strings disko-1.dd | grep "picoCTF"

After a few seconds of waiting, we get the flag
