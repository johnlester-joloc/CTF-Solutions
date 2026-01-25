# PROBLEM

<img width="608" height="521" alt="image" src="https://github.com/user-attachments/assets/c08dd084-2f75-4800-ba1c-002755327a81" />

We are given access to a remote computer. If you follow the instructions, you should gain access to the files. Inside, you will find these files:

<img width="275" height="35" alt="image" src="https://github.com/user-attachments/assets/bc418ffb-7bb5-480e-a37b-b7545f0295ec" />

**checksum.tst** contains the SHA256 hash, **decrypt.sh** is a shell script for decrypting some file, and **files** is a directory.

Checking the files inside **files**, we get this:

<img width="1537" height="310" alt="image" src="https://github.com/user-attachments/assets/f4ab6b5c-37c2-4072-abe5-4cd7ec5c6927" />

That is a lot of files to decrypt. 

# SOLUTION

Use sha256sum, which will output a checksum hash. We can run this on all the files inside **files**, then run grep to filter the file that matches

          sha256sum files/* | grep "467a10447deb3d4e17634cacc2a68ba6c2bb62a6637dad9145ea673bf0be5e02"

This will produce this result:

<img width="954" height="42" alt="image" src="https://github.com/user-attachments/assets/4d7bed5f-6ea8-4921-8892-9031a048ad3d" />

This tells us that the right file is *c6c8b911*. We can now run **decrypt.sh**

          decrypt.sh files/c6c8b911

And there's the flag
