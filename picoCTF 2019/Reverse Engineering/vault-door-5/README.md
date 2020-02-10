# vault-door-5

## Question
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: VaultDoor5.java

## Solution
From the given source code, we saw the part
```java
public boolean checkPassword(String password) {
    String urlEncoded = urlEncode(password.getBytes());
    String base64Encoded = base64Encode(urlEncoded.getBytes());
    String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                    + "JTM0JTVmJTMxJTMxJTM3JTM3JTY2JTM3JTM4JTMz";
    return base64Encoded.equals(expected);
}
```
Here we try to do the reverse of the function. Use https://www.base64decode.org/ do decode it first, then use https://www.urldecoder.org/ to decode it again. Hence, we get the flag.

flag: `picoCTF{c0nv3rt1ng_fr0m_ba5e_64_1177f783}`