# shark on wire 1


## Question
We found this packet capture. Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.


## Solution
Use Wireshark to inspect the packet. After scrolling through packet, follow those with suspicious character using Follow -> UDP Stream.

![alt text](https://github.com/aiyayayaya/ctf-writeup/blob/master/picoCTF%202019/Forensics/shark%20on%20wire%201/Capture.PNG)

flag: `picoCTF{StaT31355_636f6e6e}`
