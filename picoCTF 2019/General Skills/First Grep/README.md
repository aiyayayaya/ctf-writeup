# First Grep
## Question
Can you find the flag in file? This would be really tedious to look through manually, something tells me there is a better way. You can also find the file in /problems/first-grep_2_04dbf496b78e6c37c0097cdfef734d88 on the shell server.
## Solution
Linux Shell
```console
foo@bar:~$ wget https://2019shell1.picoctf.com/static/458ae91cb23746189bf490f0c8d9a919/file
foo@bar:~$ cat file | grep "picoCTF"
picoCTF{grep_is_good_to_find_things_bf6aec61}
```
flag: `picoCTF{grep_is_good_to_find_things_bf6aec61}`