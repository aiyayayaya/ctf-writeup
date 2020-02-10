# vault-door-7

## Question
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java

## Solution
From the source code, I first took notice of the following functions:
```java
public int[] passwordToIntArray(String hex) {
    int[] x = new int[8];
    byte[] hexBytes = hex.getBytes();
    for (int i=0; i<8; i++) {
        x[i] = hexBytes[i*4]   << 24
                | hexBytes[i*4+1] << 16
                | hexBytes[i*4+2] << 8
                | hexBytes[i*4+3];
    }
    return x;
}

public boolean checkPassword(String password) {
    if (password.length() != 32) {
        return false;
    }
    int[] x = passwordToIntArray(password);
    return x[0] == 1096770097
        && x[1] == 1952395366
        && x[2] == 1600270708
        && x[3] == 1601398833
        && x[4] == 1716808014
        && x[5] == 1734293815
        && x[6] == 1667379558
        && x[7] == 859191138;
}
```

From the code, we can the string is coverted to bytes and each element in the array contains 4 character. The number array at the end is in decimal so we need to convert it to hexadecimal and then ASCII. Use the following python code:
```python
x = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293815, 1667379558, 859191138]
string_x = ''.join([hex(i)[2:] for i in x])
for i in range(0, len(string_x), 2):
    print(chr(int(string_x[i:i+2], 16)), end='')
```

Hence, the flag is: `picoCTF{A_b1t_0f_b1t_sh1fTiNg_97cb1f367b}`