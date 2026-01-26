# PROBLEM

<img width="430" height="153" alt="image" src="https://github.com/user-attachments/assets/ee238ddf-f250-4839-b738-a48c1fbdbc71" />

We are given a problem file. Not much information is given to us

# SOLUTION

If you open the pcap file, you will find this packet with an Unknown Operation info:

<img width="1337" height="16" alt="image" src="https://github.com/user-attachments/assets/977269f3-fdac-4fe0-800e-bf206e157574" />

Inside, you will find this text:

<img width="192" height="114" alt="image" src="https://github.com/user-attachments/assets/6c003bb6-eead-4144-9454-e15a29cef741" />

It says the flag is close. I followed the stream and found nothing. I also checked for objects and found nothing

Sometimes, in CTF, the best solution is the brute force solution

I check the packets and found this section

<img width="1357" height="304" alt="image" src="https://github.com/user-attachments/assets/97d35646-b6ba-4c22-b224-8d6faf8dab47" />

There's a bunch of tcp retransmission here, and they're at len=22. However, the first packet has len=42, suggesting that there's extra data there

Open it and you'll find the flag.
