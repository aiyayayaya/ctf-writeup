# The numbers


## Question
The numbers... what do they mean?


## Solution
The given image is as follow:
![alt text](https://github.com/aiyayayaya/ctf-writeup/picoCTF "the_numbers.jpg")
It reads as `16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }` .
The first 7 numbers corresponds to PICOCTF, so now we have to write a program that convert the remaining to alphabets.


Python3
```python
>>> ''.join([chr(int(i) + ord('A') - 1) for i in "20 8 5 14 21 13 2 5 18 19 13 1 19 15 14".split(' ')])
'THENUMBERSMASON'
```
flag: `PICOCTF{THENUMBERSMASON}`
