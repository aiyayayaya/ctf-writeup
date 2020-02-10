# RSA-pop-quiz

## Question
Class, take your seats! It's PRIME-time for a quiz... nc 2019shell1.picoctf.com 30962

## Solutiom
Since this challenge is related to RSA, we need to equip ourselves with some knowledge first. [RSA](https://simple.wikipedia.org/wiki/RSA_algorithm)

When we connect to the server, we get the following:
```
Good morning class! It's me Ms. Adleman-Shamir-Rivest
Today we will be taking a pop quiz, so I hope you studied. Cramming just will not do!
You will need to tell me if each example is possible, given your extensive crypto knowledge.
Inputs and outputs are in decimal. No hex here!
#### NEW PROBLEM ####
q : 60413
p : 76753
##### PRODUCE THE FOLLOWING ####
n
IS THIS POSSIBLE and FEASIBLE? (Y/N):  
```
As we know n = pq, the answer is Y and give them n. We read through the question one by one, and come up with a [script](solve.py).

Then, we get the flag.

Flag: `picoCTF{wA8_th4t$_ill3aGal..o8227181c}`

