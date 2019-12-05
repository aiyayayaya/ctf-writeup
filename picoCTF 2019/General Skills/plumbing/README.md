# plumbing
## Question
Sometimes you need to handle process data outside of a file. Can you find a way to keep the output from this program and search for the flag? Connect to `2019shell1.picoctf.com 18944`.
## Solution
```console
foo@bar:~$ nc 2019shell1.picoctf.com 18944 | grep "pico"
picoCTF{digital_plumb3r_1d5b7de7}
```
flag: `picoCTF{digital_plumb3r_1d5b7de7}`