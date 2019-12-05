# caesar


## Question
Decrypt this message. You can find the ciphertext in /problems/caesar_1_4c9d445f770c71bd84ab0d822197a005 on the shell server.


## Solution
The name suggest a Caesar cipher. The given file contains `picoCTF{zolppfkdqeboryfzlktjxksyyl}` .
The Python script:

```python
>>> a = "zolppfkdqeboryfzlktjxksyyl"
>>> for i in range(26):
...     print(''.join([chr((ord(x) + i - ord('a')) % 26 + ord('a')) for x in a]))
...
zolppfkdqeboryfzlktjxksyyl
apmqqglerfcpszgamlukyltzzm
bqnrrhmfsgdqtahbnmvlzmuaan
crossingtherubiconwmanvbbo
dspttjohuifsvcjdpoxnbowccp
etquukpivjgtwdkeqpyocpxddq
furvvlqjwkhuxelfrqzpdqyeer
gvswwmrkxlivyfmgsraqerzffs
hwtxxnslymjwzgnhtsbrfsaggt
ixuyyotmznkxahoiutcsgtbhhu
jyvzzpunaolybipjvudthuciiv
kzwaaqvobpmzcjqkwveuivdjjw
laxbbrwpcqnadkrlxwfvjwekkx
mbyccsxqdrobelsmyxgwkxflly
nczddtyrespcfmtnzyhxlygmmz
odaeeuzsftqdgnuoaziymzhnna
pebffvatgurehovpbajznaioob
qfcggwbuhvsfipwqcbkaobjppc
rgdhhxcviwtgjqxrdclbpckqqd
sheiiydwjxuhkrysedmcqdlrre
tifjjzexkyvilsztfendremssf
ujgkkafylzwjmtaugfoesfnttg
vkhllbgzmaxknubvhgpftgouuh
wlimmchanbylovcwihqguhpvvi
xmjnndiboczmpwdxjirhviqwwj
ynkooejcpdanqxeykjsiwjrxxk
```
`"crossingtherubiconwmanvbbo"` looks like the right answer.
Flag: `picoCTF{crossingtherubiconwmanvbbo}`