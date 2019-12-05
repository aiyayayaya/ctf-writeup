# Glory of the Garden


## Question
This garden contains more than it seems. You can also find the file in /problems/glory-of-the-garden_1_2e13eb26e18a569a71cc32f9d51ccb4e on the shell server.


## Solution
```console
foo@bar:~$ wget https://2019shell1.picoctf.com/static/d0c77bdcf4a77a0ba60820fc22404584/garden.jpg
foo@bar:~$ strings garden.jpg | grep "pico"
Here is a flag "picoCTF{more_than_m33ts_the_3y3b7FBD20b}"
```
flag: `picoCTF{more_than_m33ts_the_3y3b7FBD20b}`