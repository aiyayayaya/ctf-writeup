# easy1


## Question
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help `UFJKXQZQUNB` with the key of `SOLVECRYPTO`. Can you use this table to solve it?.


## Solution
The given cipher is Vigenere cipher. See [here](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)


#### Python3
```python
>>> ''.join([chr((ord(a[i]) - ord(b[i]) - ord('A') * 2) % 26 + ord('A')) for i in range(len(a))])
'CRYPTOISFUN'
```
flag: `picoCTF{CRYPTOISFUN}`
