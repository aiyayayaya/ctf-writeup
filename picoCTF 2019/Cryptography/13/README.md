# 13


## Question
Cryptography can be easy, do you know what ROT13 is? cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}


## Solution
ROT13 means the alphabets are shifted by 13 characters.
Python3
```python
>>> ''.join([chr((ord(i) + 13 - ord('a')) % 26 + ord('a')) for i in "abggbbonqbsnceboyrz"])
'nottoobadofaproblem'
```
flag: `picoCTF{not_too_bad_of_a_problem}`