# 1_wanna_b3_a_r0ck5tar

## Question
I wrote you another song. Put the flag in the picoCTF{} flag format

## Solution
The given file looks like a rockstar problem, similar to the mus1c challenge. Using the [Doc](https://codewithrockstar.com/docs), we translate it as follow:
```
Rocknroll is right                          (Rocknroll = True)
Silence is wrong                            (Silence = wrong)
A guitar is a six-string                    (A guitar = 10)
Tommy's been down                           (Tommy = 44)
Music is a billboard-burning razzmatazz!    (Music = 170)
Listen to the music                         (the music = INPUT)
If the music is a guitar                    (the music = 10)
Say "Keep on rocking!"                      (print "Keep on rocking!")
Listen to the rhythm                        (rhythm = INPUT)
If the rhythm without Music is nothing      (if rhythm - Music = 0)
Tommy is rockin guitar                      (Tommy = 66)
Shout Tommy!                                (print Tommy)
Music is amazing sensation                  (Music = 79)
Jamming is awesome presence                 (Jamming = 78)
Scream Music!                               (print Music)
Scream Jamming!                             (print Jamming)
Tommy is playing rock                       (Tommy = 74)
Scream Tommy!                               (print Tommy)
They are dazzled audiences                  (Tommy = 79)
Shout it!                                   (print Tommy)
Rock is electric heaven                     (Rock = 86)
Scream it!                                  (print Rock)
Tommy is jukebox god                        (Tommy = 73)
Say it!                                     (print Tommy)
Break it down                               (Tommy -= 1)
Shout "Bring on the rock!"                  (print "Bring on the rock!")
Else Whisper "That ain't it, Chief"         (else print "That ain't it, Chief")
Break it down                               (Tommy -= 1)
```

By [running the program](https://codewithrockstar.com/online) with input 
```
10
170
```
we get the following:
```
Keep on rocking!
66
79
78
74
79
86
73
```

Using python3 to decode them as ASCII:
```python
>>> a = """66
... 79
... 78
... 74
... 79
... 86
... 73""".split("\n")
>>> a
['66', '79', '78', '74', '79', '86', '73']
>>> ''.join([chr(int(i)) for i in a])
'BONJOVI'
```

Flag: `picoCTF{BONJOVI}`

