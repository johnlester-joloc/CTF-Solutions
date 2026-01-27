# PROBLEM

<img width="599" height="150" alt="image" src="https://github.com/user-attachments/assets/201f13b0-99a7-4ae1-8796-52b78caa889e" />

We are given two files: a locked zip file and a pcap file

# SOLUTION

If you try opening the flag.zip, you will find that it is locked

<img width="461" height="165" alt="image" src="https://github.com/user-attachments/assets/4bdae3ce-a15e-4ed7-ae04-2b80220cab3c" />

We need some kind of password. Let's check the pcap file using Wireshark

The first 9 packets are dupes designed to throw us off. I tried using the text "Flying on Ethernet secret" as the password, but it did not work

<img width="207" height="126" alt="image" src="https://github.com/user-attachments/assets/dc7f768a-86b6-42a2-98f4-d832153cc30c" />

We find another batch of packets that contain a clue

<img width="953" height="292" alt="image" src="https://github.com/user-attachments/assets/61d93fd2-f046-45c0-9208-003b3bdf81da" />

<img width="187" height="94" alt="image" src="https://github.com/user-attachments/assets/292f4846-702f-42ec-a8bb-6150bd17de40" />

It seems part of the flag might be in this pcap file

Eventually,  I found this mysterious packet with a trailing '=', which means it is in base64

<img width="1051" height="474" alt="image" src="https://github.com/user-attachments/assets/7ee42672-16ae-435a-9189-f33411dba8f5" />

Clicking on the data section highlights this part of the packet

<img width="669" height="207" alt="image" src="https://github.com/user-attachments/assets/b331a1d9-e018-48c2-ae93-5b00887a70ab" />

          VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=

Decode it using base64

          echo "VGhpcyBpcyB0aGUgc2VjcmV0OiBwaWNvQ1RGe1IzNERJTkdfTE9LZF8=" | base64 -d

You will get half of the flag (I will not show it here). We need the other half

We find another clue here

<img width="971" height="186" alt="image" src="https://github.com/user-attachments/assets/7f77b540-44f9-4301-8946-2464ccf38709" />

<img width="664" height="114" alt="image" src="https://github.com/user-attachments/assets/7e588194-86b4-4f3e-a89c-fe45c1b54834" />

Since we have half of the flag, it only makes sense that the other half is in the locked file. Let's try using the half-flag as the password

And it worked, open it to get the flag
