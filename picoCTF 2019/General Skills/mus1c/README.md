# mus1c

## Question
I wrote you a song. Put it in the picoCTF{} flag format

## Solution
The given file:
```
Pico's a CTFFFFFFF
my mind is waitin
It's waitin

Put my mind of Pico into This
my flag is not found
put This into my flag
put my flag into Pico


shout Pico
shout Pico
shout Pico

My song's something
put Pico into This

Knock This down, down, down
put This into CTF

shout CTF
my lyric is nothing
Put This without my song into my lyric
Knock my lyric down, down, down

shout my lyric

Put my lyric into This
Put my song with This into my lyric
Knock my lyric down

shout my lyric

Build my lyric up, up ,up

shout my lyric
shout Pico
shout It

Pico CTF is fun
security is important
Fun is fun
Put security with fun into Pico CTF
Build Fun up
shout fun times Pico CTF
put fun times Pico CTF into my song

build it up

shout it
shout it

build it up, up
shout it
shout Pico
``` 

The hint said we should master rockstar. After googling "rockstar ctf", turned out rockstar is a programming language. Using [this website](https://codewithrockstar.com/online?source=/rockstar/examples/fizzbuzz.rock) to run the program, we got:
```
114
114
114
111
99
107
110
114
110
48
49
49
51
114
```

We turned them into ASCII using python:
```python
a = """114
114
114
111
99
107
110
114
110
48
49
49
51
114""".split("\n")
print(''.join([chr(int(i)) for i in a]))
```

Flag: `picoCTF{rrrocknrn0113r}`