# Strings it
## Question
Can you find the flag in file without running it? You can also find the file in /problems/strings-it_3_8386a6aa560aecfba03c0c6a550b5c51 on the shell server.
## Solution
```console
foo@bar:~$ wget https://2019shell1.picoctf.com/static/e93edd77d319a5a634cd4d20159cbc1d/strings
foo@bar:~$ strings strings | grep "pico"
picoCTF{5tRIng5_1T_c7fff9e5}
``` 
flag: `picoCTF{5tRIng5_1T_c7fff9e5}`