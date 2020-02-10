# vault-door-8

## Question
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: VaultDoor8.java

## Solution
When I first saw the source code, it is not formatted. I used the code formatting function in Visual Studio Code to pretty print it. There were three function to be noticed here:
```java
public char[] scramble(String password) {/* Scramble a password by transposing pairs of bits. */
    char[] a = password.toCharArray();
    for (int b = 0; b < a.length; b++) {
        char c = a[b];
        c = switchBits(c, 1, 2);
        c = switchBits(c, 0, 3);
        /* c = switchBits(c,14,3); c = switchBits(c, 2, 0); */ 
        c = switchBits(c, 5, 6);
        c = switchBits(c, 4, 7);
        c = switchBits(c, 0, 1);
        /* d = switchBits(d, 4, 5); e = switchBits(e, 5, 6); */ 
        c = switchBits(c, 3, 4);
        c = switchBits(c, 2, 5);
        c = switchBits(c, 6, 7);
        a[b] = c;
    }
    return a;
}

public char switchBits(char c, int p1, int p2) {
    /*
    * Move the bit in position p1 to position p2, and move the bit that was in
    * position p2 to position p1. Precondition: p1 < p2
    */ 
    char mask1 = (char) (1 << p1);
    char mask2 = (char) (1 << p2);
    /* char mask3 = (char)(1<<p1<<p2); mask1++; mask1--; */ 
    char bit1 = (char) (c & mask1);
    char bit2 = (char) (c & mask2);
    /*
    * System.out.println("bit1 " + Integer.toBinaryString(bit1));
    * System.out.println("bit2 " + Integer.toBinaryString(bit2));
    */ 
    char rest = (char) (c & ~(mask1 | mask2));
    char shift = (char) (p2 - p1);
    char result = (char) ((bit1 << shift) | (bit2 >> shift) | rest);
    return result;
}

public boolean checkPassword(String password) {
    char[] scrambled = scramble(password);
    char[] expected = { 0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4,
            0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC1, 0xF1, 0xD0, 0x95, 0x94, 0xD1, 0xA5, 0xC2, 0xD0 };
    return Arrays.equals(scrambled, expected);
}
```

Basically, function switchBits does as it say, and we need to restore the byte array and turn it to ASCII. Using the following code:
```python
a = [0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0xC1, 0xF1, 0xD0, 0x95, 0x94, 0xD1, 0xA5, 0xC2, 0xD0]
b = []
for i in a:
    temp = list(bin(i)[2:])
    while len(temp) < 8:
        temp.insert(0, '0')
    temp[6], temp[7] = temp[7], temp[6]
    temp[2], temp[5] = temp[5], temp[2]
    temp[3], temp[4] = temp[4], temp[3]
    temp[0], temp[1] = temp[1], temp[0]
    temp[4], temp[7] = temp[7], temp[4]
    temp[5], temp[6] = temp[6], temp[5]
    temp[3], temp[0] = temp[0], temp[3]
    temp[1], temp[2] = temp[2], temp[1]
    print(chr(int(''.join(temp), 2)), end='')
```
The flag is: `picoCTF{s0m3_m0r3_b1t_sh1fTiNg_471ea5f81}`