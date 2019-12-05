# tapping


## Question
Theres tapping coming in from the wires. What's it saying `nc 2019shell1.picoctf.com 37911`.


## Solution
When we connect to the server,
```console
foo@bar:~$ nc 2019shell1.picoctf.com 37911
.--. .. -.-. --- -.-. - ..-. { -- ----- .-. ... ...-- -.-. ----- -.. ...-- .---- ... ..-. ..- -. ..--- ..--- -.... ..... ----. ...-- --... -.... -.... ...-- }
```


This is Morse code obviously, so we can use this [link](https://morsecode.scphillips.com/translator.html) to translate it.
flag: `PICOCTF{M0RS3C0D31SFUN2265937663}`
