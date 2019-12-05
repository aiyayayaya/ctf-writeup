# First Grep Part II


## Question
Can you find the flag in /problems/first-grep--part-ii_6_84224d7d745e41d24bde7e7bc7062bbe/files on the shell server? Remember to use grep.


## Solution
On the official shell:
```console
foo@pico-2019-shell1:~$ cd /problems/first-grep--part-ii_6_84224d7d745e41d24bde7e7bc7062bbe/
foo@pico-2019-shell1:/problems/first-grep--part-ii_6_84224d7d745e41d24bde7e7bc7062bbe$ grep -Hrn "picoCTF" files
files/files2/file24:2:picoCTF{grep_r_to_find_this_5241c61f}
```


flag: `picoCTF{grep_r_to_find_this_5241c61f}`