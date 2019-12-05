# where-is-the-file
## Question
I've used a super secret mind trick to hide this file. Maybe something lies in /problems/where-is-the-file_2_f1aa319cafd4b55ee4a60c1ba65255e2.
## Solution
On official shell:
```console
foo@pico-2019-shell1:~$ cd /problems/where-is-the-file_2_f1aa319cafd4b55ee4a60c1ba65255e2
foo@pico-2019-shell1:/problems/where-is-the-file_2_f1aa319cafd4b55ee4a60c1ba65255e2$ ls -a
.  ..  .cant_see_me
foo@pico-2019-shell1:/problems/where-is-the-file_2_f1aa319cafd4b55ee4a60c1ba65255e2$ cat .cant_see_me 
picoCTF{w3ll_that_d1dnt_w0RK_30444bc6}
```
flag: `picoCTF{w3ll_that_d1dnt_w0RK_30444bc6}`