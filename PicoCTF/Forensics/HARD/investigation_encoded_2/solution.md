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

A char variale is initialized 




