# PROBLEM

<img width="627" height="257" alt="image" src="https://github.com/user-attachments/assets/79d59b68-0e57-424d-902e-2659b0289ce7" />

We are given a binary file and an image. We will use forensics and reverse engineering skills here.

# SOLUTION

First we will view the image file.

          xxd output | head

<img width="589" height="83" alt="image" src="https://github.com/user-attachments/assets/6c14eff9-b295-4a71-be73-5bcccc81957c" />

This is an interesting file. We need more context 

          file output

<img width="526" height="31" alt="image" src="https://github.com/user-attachments/assets/125c8d10-7462-48fd-9759-bf0da99e5300" />

It seems to be an ASCII text, but this can easily be a misdirection. Let us now run Ghidra and reverse engineer the binary

## Open Ghidra

Open the file tab in Ghidra

<img width="984" height="738" alt="image" src="https://github.com/user-attachments/assets/fe52531f-c10e-41a5-bbc6-2f4d0193145a" />

Select New Project

<img width="631" height="463" alt="image" src="https://github.com/user-attachments/assets/dcff5ec6-2233-4d1b-93c7-b2abf47358e5" />

Click Next

<img width="628" height="476" alt="image" src="https://github.com/user-attachments/assets/8dfc4845-59e5-465a-93f5-bf43a9e4209e" />

Change the Project Directory to any folder you like (I recommend a new folder inside your problem folder) and click Next

Click File again

<img width="978" height="738" alt="image" src="https://github.com/user-attachments/assets/19f179c0-aa1f-4db3-ae3d-c6d5e25bb29a" />

This time, click Import File. Import the right file 

<img width="616" height="312" alt="image" src="https://github.com/user-attachments/assets/ace7d5b3-c7c9-4bc4-a163-d9a1f358bfc9" />

Select OK

<img width="1005" height="1073" alt="image" src="https://github.com/user-attachments/assets/e7482ed9-6e02-4cdb-99c4-58f7f466229d" />

Click OK. Click the Imported File

Analyze the File. In Analysis, select Auto Analysis to analyze the file

<img width="1224" height="744" alt="image" src="https://github.com/user-attachments/assets/2b940adc-593e-44a3-b0d8-18f2000dbba6" />

You should now be able to decompile the file.

## Main Function Analysis

<img width="943" height="785" alt="image" src="https://github.com/user-attachments/assets/c6364d9a-4aab-4b38-9822-80300e31fff1" />

Look at the main function. They opened a file "flag.txt" in read mode

<img width="565" height="166" alt="image" src="https://github.com/user-attachments/assets/6056be13-61ff-45da-adfb-f365e1ace518" />

A set of interesting operations were done here

<img width="258" height="119" alt="image" src="https://github.com/user-attachments/assets/cd9f6d17-e46e-4267-8d2e-bdf154f1be8e" />

First, they used *fseek()*. *fseek()* is used to move the file pointer from one byte to another. *fseek()* is defined like this

          int fseek(FILE *stream, long offset, int whence)

`stream: The file`
`offset: the amount in bytes to offset the file pointer`
`whence: an ENUM, used to identify the beginning of the offset`

The **whence** parameter accepts 3 possible values. `SEEK_SET` (0), `SEEK_CUR` (1), and `SEEK_END` (2). Here, they used `SEEK_END`, meaning the pointer was moved to the end of the file.

Then they stored the file pointer location using *ftell()* to **1Var1**. The **flag_size** is then set to **1Var1**.

<img width="726" height="228" alt="image" src="https://github.com/user-attachments/assets/0de1eabe-c6d4-44cf-854d-d0abfc90b479" />

This section above tells us that the **flag_size** must be 10.

Some variables are initialized, mainly the output file and the **flag_index**

<img width="309" height="136" alt="image" src="https://github.com/user-attachments/assets/776c0495-4bf0-4c6a-a71b-0ee3d25089c1" />

And then an *encode()* function is called, likely to write the flag to our output file

<img width="167" height="48" alt="image" src="https://github.com/user-attachments/assets/0e1af5c6-ddf8-49c7-8b56-0154faf4a602" />

## Encode Function Analysis

The *encode()* function has a conditional while loop inside

<img width="799" height="661" alt="image" src="https://github.com/user-attachments/assets/fc496115-c1b8-4ad8-ba8c-b4dc8e15310b" />

Let's dissect this while loop to understand what is happening to our flag.

The condition is here. Recall that **flag_size** is set to 10.

<img width="329" height="32" alt="image" src="https://github.com/user-attachments/assets/42f6f283-159f-4862-ad07-00e77fb9dc3e" />

The update is not bound by soem condition

<img width="301" height="25" alt="image" src="https://github.com/user-attachments/assets/4e4c8543-dd2b-4e22-bcb1-2aa73126be35" />

This means our while loops has to occur only 10 times.

A char variale is initialized. It is the nth char in our flag, but it is the output of a function *lower*

<img width="486" height="24" alt="image" src="https://github.com/user-attachments/assets/0c0d5749-ea0a-4229-b865-1d64880a8a08" />

This is not the same as *toLower()* of *stdio.h*, this is a custom one. Let us dissect it.

### Lower Function Analysis

<img width="502" height="304" alt="image" src="https://github.com/user-attachments/assets/07b950de-bcd8-4528-825d-1f429b90c11f" />

It seems to function just the same as *toLower()*

Next we will look at how it encodes the characters. The first section is this

<img width="267" height="70" alt="image" src="https://github.com/user-attachments/assets/28441381-9c32-4242-a73e-b9eaf5828b55" />

Whitespaces are offset by '-0x7b'

<img width="453" height="69" alt="image" src="https://github.com/user-attachments/assets/2b32f76d-bf7e-4359-9a99-b4815e72d348" />

Characters between '/' and ':' are offset by +'K'

<img width="313" height="21" alt="image" src="https://github.com/user-attachments/assets/95b85a48-a910-4c25-890e-6a99c1f1741b" />

Then every character is offset by '-0x71'

<img width="438" height="71" alt="image" src="https://github.com/user-attachments/assets/ba4675a6-05e6-4bdf-bd07-9afc8c952436" />

Then it checks for 'badChar'. Negative numbers are labeled as 'badChar', same as chars greater than '$'. This happens after the first encoding

<img width="413" height="115" alt="image" src="https://github.com/user-attachments/assets/a44a9e31-2cfb-4fef-9cdc-9f5a2e96e17e" />

Then it finds all chars that are not '$'. It does some crazy offsetting

<img width="309" height="23" alt="image" src="https://github.com/user-attachments/assets/f8d92629-33d0-40d0-b46b-0674b8c88625" />

First it adds 0x12, then MODs it by 0x24.

<img width="308" height="22" alt="image" src="https://github.com/user-attachments/assets/eb51ee75-856d-46ba-99a8-a881f18b359e" />

Then it bitshifts it by 0x1f

<img width="390" height="25" alt="image" src="https://github.com/user-attachments/assets/dcf23b3e-79ad-45db-92e7-b0e56953b2ac" />

Finally, the char is computed by this line.

<img width="514" height="19" alt="image" src="https://github.com/user-attachments/assets/abde6dae-2b09-47e0-b845-2c5837a8f39a" />

Then it computes this value iVar3

<img width="760" height="117" alt="image" src="https://github.com/user-attachments/assets/1f09506d-38fb-47e0-bc4e-c83bca19e5e5" />

Then this for loop, occurs. I am not exactly sure of how this works, there are variables here that can't be found anywhere

<img width="276" height="24" alt="image" src="https://github.com/user-attachments/assets/c9eb4f34-7b7a-4610-89f7-e0cda77ade74" />

This section of the for loop computes some kind of value. Let us investigate this function.

### GetValue Function Analysis

<img width="797" height="300" alt="image" src="https://github.com/user-attachments/assets/cde0495f-9e52-4560-8908-c633fcb5d061" />

I notice that it returns an unsigned int. There's also this section:

<img width="229" height="61" alt="image" src="https://github.com/user-attachments/assets/74a1d9fb-9534-48f3-bc30-2153a644e431" />

It adds 7 to negative values. This could mean that negative numbers are only upto -7

<img width="789" height="24" alt="image" src="https://github.com/user-attachments/assets/7ec3e9af-11a7-4d1e-8f71-b7d0848b161e" />

Then we have this section with plenty of bit manipulations

<img width="141" height="28" alt="image" src="https://github.com/user-attachments/assets/67fda776-1293-4d6a-b55f-f4c451df5c5b" />

Then it runs this *save()* function

### Save Function Analysis

<img width="359" height="351" alt="image" src="https://github.com/user-attachments/assets/508a7bc6-4362-4447-b25b-bf256512eedb" />

The purpose of this function is to save the characters to the output file.

<img width="318" height="26" alt="image" src="https://github.com/user-attachments/assets/912bb35b-9a62-4ba8-ab5e-e3db685f3f90" />

It runs bit manipulation on the buffChar

<img width="353" height="112" alt="image" src="https://github.com/user-attachments/assets/855aaffe-c848-4985-b6f2-42f44a0d83dd" />

Then it tries to save it when remain is 0

<img width="313" height="96" alt="image" src="https://github.com/user-attachments/assets/7650e378-42d4-44fa-8f22-2ec24bc89e0d" />

If remains is not 0, it multiplies tha value by 0x02

Outside the while loop, it tries to run this

<img width="301" height="71" alt="image" src="https://github.com/user-attachments/assets/03c9f715-f71f-4297-823b-a0767cd8a854" />

## Testing the Executable

Before we can reverse engineer it, let us run the executable using our own flag. I moved the executable to its own folder. 

With a flag content of 10 zeroes, this is what we get:

<img width="158" height="34" alt="image" src="https://github.com/user-attachments/assets/a1f8d9f8-26e8-48fd-a2aa-bf3abc55a89b" />

With 10 'a', it gives us this

<img width="191" height="28" alt="image" src="https://github.com/user-attachments/assets/be04daa9-c62d-4e2a-a60d-d75063521dc0" />

With 10 'z', we get this

<img width="316" height="42" alt="image" src="https://github.com/user-attachments/assets/a278e1df-11e5-4976-83ca-87de8053f4e8" />


The behavior of this is clear, each flag character is offset so much it goes beyond the 8 bit ASCII limit, which is why there is an overflow and why it displayes UNICODE characters instead

## Reversing

I will write a Python script that reverses the contents of the output file.


