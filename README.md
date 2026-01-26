# CTF Solutions

This repository is dedicated for storing my own CTF Solutions from various CTF Challenges websites. Simply navigate the directory to find the solution to a CTF you're struggling on. The flag is not included (don't be silly).

## WEBSITES COVERED
* [PicoCTF](https://play.picoctf.org/)

## INCLUDED IN THE SOLUTIONS FOLDER
1. Problem File
2. solution.md
3. Any scripts used

## NOT INCLUDED IN THE SOLUTIONS FOLDER
1. The flag (The instructions are literally there, don't be lazy)
2. Extracted files

## TOOLS

### Operating System
- Kali Linux (using WSL)

### Forensics
| Tool | Use | Installation |
| :--- | :--- | :--- |
|exiftool| Checking file metadata | `sudo apt install exiftool` |
|file| Checking file type and file information| Pre-installed |
|grep| Output filtering| Pre-installed |
|cat| Output file contents| Pre-installed |
|strings|Checking strings inside files| Pre-installed|
|xxd| For hexdunp | Pre-installed|
|hexedit| Editing hex bytes | `sudo apt install hexedit` |
|fdisk| Checking disc images for partitions | Pre-installed |
|Autopsy| File system analysis | [Install Autopsy](https://www.autopsy.com/download/)

### Steganography
| Tool | Use | Installation |
| :--- | :--- | :--- |
|zsteg| Checking LSB of png files| `sudo gem install zsteg` |
|steghide| Extracting data hidden using steghide| `sudo apt install steghide`|
|StegOnline| General purpose steganography | [StegOnline](https://georgeom.net/StegOnline/upload)|

### Networks
| Tool | Use | Installation |
| :--- | :--- | :--- |
|WireShark| General-purpose network traffic inspection| [Install WireShark](https://www.wireshark.org/download.html)|
|tshark| CLI-version of WireShark| [Install WireShark](https://www.wireshark.org/download.html)|

### Reverse Engineering
| Tool | Use | Installation |
| :--- | :--- | :--- |
|Ghidra|Decompiling executable files to equivalent C code| [Install Ghidra](https://ghidralite.com/)|


**Note: still adding solutions from my OG WriteUp document**



