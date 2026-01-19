# PROBLEM

<img width="618" height="488" alt="image" src="https://github.com/user-attachments/assets/d735d4eb-e9e8-45ac-a3fb-7687c672eeb5" />

We are given a network packet capture file. The flag is most likely hidden in the packets

# SOLUTION

You need [Wireshark](https://www.wireshark.org/download.html) to do this. Open the pcap file in wireshark

We can find packets with TCP protocol. On the Info tab, you'll see a text "Len=8". There are also Len=12 and Len=4. If you click on one of them, you'll see something like this:

<img width="862" height="390" alt="image" src="https://github.com/user-attachments/assets/c260126e-dfa3-4a26-b791-6a5e495a636a" />

The first bytes are most likely related to the packet itself and not the packet data. However, we can see strings in the base64 format at the end

          ZTEwZTgzOQ==

Interestingly enough, only the packets with Len=12 and Len=4 contain base64 string ("==" at the end). Let us extract each of them one by one, sorted by time.
Right click on the data and select "..as ASCII Text". MAKE SURE TO COPY ONLY THE LAST TEXT (after the last ".."), JUST DELETE THE REST OF THE TEXT (or you can type it yourself)

``cGljb0NURg==``
``ezF0X3c0cw==``
``bnRfdGg0dA==``
``XzM0c3lfdA==``
``YmhfNHJfOA==``
``ZTEwZTgzOQ==``
``fQ==``

Connect them together and we get

          cGljb0NURg==ezF0X3c0cw==bnRfdGg0dA==XzM0c3lfdA==YmhfNHJfOA==ZTEwZTgzOQ==fQ==

Using base64 to decode it

          echo cGljb0NURg==ezF0X3c0cw==bnRfdGg0dA==XzM0c3lfdA==YmhfNHJfOA==ZTEwZTgzOQ==fQ== | base64 -d

And you get the flag...but this is such a sloppy solution, imagine if we had hundreds of packets to check for?

# ELEGANT SOLUTION

You will need Tshark for this, which is the CLI version of [Wireshark](https://www.wireshark.org/download.html) (don't worry, it's part of the wireshark application)

Since we care only about the packets that are of Len=12 and Len=4, we must filter the packet. The format is like this

          tshark -r <file> -Y <filter>
In this case, it will be like this

          tshark -r myNetworkTraffic.pcap -Y "tcp.len == 12 || tcp.len == 4"

This will give us the packets. However, we only care about the following: the segment data, and the time (to sort it). For this, we will use the -T argument

          ... -T fields -e <field> -e <field> -e <field>... -e <field>
Or in our case

          -T fields -e tcp.segment_data -e frame.time

Combining the commands, you should get something like this

<img width="584" height="146" alt="image" src="https://github.com/user-attachments/assets/d30779ac-48af-4563-a827-83bc7a312a85" />

However, it isn't sorted. We must sort it using the sort command

        sort -k<nth column>
Or in this case

        sort -k4

You should now get something like this

<img width="898" height="141" alt="image" src="https://github.com/user-attachments/assets/27069016-011b-46bf-ad62-f8de43dcad67" />

Still, the output is not the flag yet. For that, we must extract **only the data segment**. For that, we must use the awk command

          awk '{print $<nth string}'
And since the data (in hex) is the first string per line

          awk '{print $1}'

You should get something like this:

<img width="268" height="131" alt="image" src="https://github.com/user-attachments/assets/954ac27b-4805-4cae-9c1f-38c560c5897b" />

We're getting closer. The printed output is in hex, so we must convert it using xxd

          xxd -r -p

``-r: revert, revert the hexcode``

``-p: print plainly``

You should now get the base64 string

          cGljb0NURg==ezF0X3c0cw==bnRfdGg0dA==XzM0c3lfdA==YmhfNHJfOA==ZTEwZTgzOQ==fQ==
Convert it to base64

          echo "cGljb0NURg==ezF0X3c0cw==bnRfdGg0dA==XzM0c3lfdA==YmhfNHJfOA==ZTEwZTgzOQ==fQ==" | base64 -d

And you get the flag

Combining all of the commands, we can get the flag in one line of commands through piping

          tshark -r myNetworkTraffic.pcap -Y "tcp.len == 12 || tcp.len == 4" -T fields -e tcp.segment_data -e frame.time | sort -k4 | awk '{print $1}' | xxd -r -p | base64 -d





