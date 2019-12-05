from pwn import *

def decrypt_with_key(str, key):
    result = ""
    for char in str:
        #shift each character key places later in the alphabet,
        #wrapping from Z back to A if necessary
        newchar = chr(((ord(char) - key + ord('A')) % 26) + ord('A'))
        result += newchar
    return result


p = remote("chal.tuctf.com", 30100)
msg = p.recv().decode("ascii").split("\n")[-2].split(" ")[-1]
for i in range(1, 27):
    print(decrypt_with_key(msg, i))
    p.sendline(decrypt_with_key(msg, i))
p.interactive()
print(msg)