# miniRSA

## Question
Lets decrypt this: ciphertext? Something seems a bit small

## Solution
From the hints, it seems like the e is quite small. From [this link](https://crypto.stackexchange.com/questions/18301/textbook-rsa-with-exponent-e-3), it seems like we can recover the plaintext directly. Note that precision matters here, so we need to find a way to deal with large numbers. In python, integers have infinite precision so we use binary search to find the cube root. 

```python
ciphertext = 2205316413931134031074603746928247799030155221252519872649604243394069216326314270624430181767863085854215545736160599718939066687544261205735290002239045830806570632200667142910415788763317978137702614731825117431700919216297401306846053
def find_invpow(x,n):
    """Finds the integer component of the n'th root of x,
    an integer such that y ** n <= x < (y + 1) ** n.
    """
    high = 1
    while high ** n < x:
        high *= 2
    low = high // 2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid ** n < x:
            low = mid
        elif high > mid and mid ** n > x:
            high = mid
        else:
            return mid
    return mid + 1

print(bytearray.fromhex(hex(find_invpow(ciphertext, 3))[2:]).decode())
```

flag: `picoCTF{n33d_a_lArg3r_e_1dcea0a2}`