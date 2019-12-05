# Bases
## Question
What does this `bDNhcm5fdGgzX3IwcDM1` mean? I think it has something to do with bases.

## Solution
Python3
```python
>>> import base64
>>> base64.b64decode('bDNhcm5fdGgzX3IwcDM1')
b'l3arn_th3_r0p35'
```
Flag: `picoCTF{l3arn_th3_r0p35}`
