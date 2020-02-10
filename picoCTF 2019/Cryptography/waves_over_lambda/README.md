# waves over lambda

## Question

## Solution
After connecting to the server, we received a chunk of text. 
```
-------------------------------------------------------------------------------
opzclrqn fili yn kpvl wurc - wlidvizok_yn_o_pmil_urgjxr_wxyyylvjlr
-------------------------------------------------------------------------------
frmyzc frx npgi qygi rq gk xynepnru bfiz yz upzxpz, y frx mynyqix qfi jlyqynf gvnivg, rzx grxi nirlof rgpzc qfi jpptn rzx gren yz qfi uyjlrlk licrlxyzc qlrznkumrzyr; yq frx nqlvot gi qfrq npgi wplitzpbuixci pw qfi opvzqlk opvux frlxuk wryu qp frmi npgi ygeplqrzoi yz xiruyzc byqf r zpjuigrz pw qfrq opvzqlk. y wyzx qfrq qfi xynqlyoq fi zrgix yn yz qfi iaqligi irnq pw qfi opvzqlk, svnq pz qfi jplxiln pw qflii nqrqin, qlrznkumrzyr, gpuxrmyr rzx jvtpmyzr, yz qfi gyxnq pw qfi orlerqfyrz gpvzqryzn; pzi pw qfi byuxinq rzx uirnq tzpbz eplqypzn pw ivlpei. y brn zpq rjui qp uycfq pz rzk gre pl bplt cymyzc qfi iaroq uporuyqk pw qfi ornqui xlrovur, rn qfili rli zp gren pw qfyn opvzqlk rn kiq qp opgerli byqf pvl pbz plxzrzoi nvlmik gren; jvq y wpvzx qfrq jynqlyqh, qfi epnq qpbz zrgix jk opvzq xlrovur, yn r wryluk biuu-tzpbz euroi. y nfruu izqil fili npgi pw gk zpqin, rn qfik grk liwlinf gk gigplk bfiz y qrut pmil gk qlrmiun byqf gyzr.
```

As the hints said it is a substitution cipher, lets use online tools to do a frequency analysis. Using [this website](https://www.dcode.fr/monoalphabetic-substitution), we were able to decrypt the text and get the flag. 

```
CONGRATS HERE IS YOUR FLAG - FREQUENCY_IS_C_OVER_LAMBDA_FDIIIRUBRA HAVING HAD SOME TIME AT MY DISPOSAL WHEN IN LONDON, I HAD VISITED THE BRITISH MUSEUM, AND MADE SEARCH AMONG THE BOOKS AND MAPS IN THE LIBRARY REGARDING TRANSYLVANIA; IT HAD STRUCK ME THAT SOME FOREKNOWLEDGE OF THE COUNTRY COULD HARDLY FAIL TO HAVE SOME IMPORTANCE IN DEALING WITH A NOBLEMAN OF THAT COUNTRY. I FIND THAT THE DISTRICT HE NAMED IS IN THE EXTREME EAST OF THE COUNTRY, JUST ON THE BORDERS OF THREE STATES, TRANSYLVANIA, MOLDAVIA AND BUKOVINA, IN THE MIDST OF THE CARPATHIAN MOUNTAINS; ONE OF THE WILDEST AND LEAST KNOWN PORTIONS OF EUROPE. I WAS NOT ABLE TO LIGHT ON ANY MAP OR WORK GIVING THE EXACT LOCALITY OF THE CASTLE DRACULA, AS THERE ARE NO MAPS OF THIS COUNTRY AS YET TO COMPARE WITH OUR OWN ORDNANCE SURVEY MAPS; BUT I FOUND THAT BISTRITZ, THE POST TOWN NAMED BY COUNT DRACULA, IS A FAIRLY WELL-KNOWN PLACE. I SHALL ENTER HERE SOME OF MY NOTES, AS THEY MAY REFRESH MY MEMORY WHEN I TALK OVER MY TRAVELS WITH MINA.
```

Before submitting, we have to turn all the text into lower case by doing:
```python
s = "FREQUENCY_IS_C_OVER_LAMBDA_FDIIIRUBRA"
print(''.join([a.lower() for a in s]))
```

flag: `frequency_is_c_over_lambda_fdiiirubra`