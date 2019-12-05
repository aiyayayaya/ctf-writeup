from pwn import *
import string
import difflib

p = remote("chal.tuctf.com", 30102)

decrypt = ['Give']
for i in range(5):
    #level 0
    print(i)
    p.recv(timeout=2)
    p.sendline(string.ascii_lowercase)
    cipher = p.recvline(timeout=2).decode("ascii")[:-1].split(" ")[3:]
    print(cipher)
    p.recvline(timeout=2)
    decrypt = p.recv(timeout=2).decode("ascii").split("\n")[-2].split(" ")

    while 'Decrypt' in decrypt:
        decrypt = decrypt[1:]
        print(decrypt)
        answer = ''
        for word in decrypt:
            answer += chr(cipher.index(difflib.get_close_matches(word, cipher)[0]) + ord('A'))
        print("answer: " + answer)
        p.sendline(answer)
        decrypt = p.recv(timeout=5).decode("ascii").split("\n")[-2].split(" ")
        if len(decrypt) == 1:
            decrypt = p.recv(timeout=5).decode("ascii").split("\n")[-2].split(" ")  
        print(decrypt)

p.recv(timeout=2)
p.sendline(string.ascii_letters[26:] + string.ascii_letters[:26])
cipher = p.recvline(timeout=2).decode("ascii")[:-1].split(" ")[3:]
print(cipher)
p.recvline(timeout=2)
decrypt = p.recv(timeout=2).decode("ascii").split("\n")[-2].split(" ")

decrypt = decrypt[1:]
print(decrypt)
answer = ''
close = []
for word in decrypt:
    try:
        indices = [i for i, x in enumerate(cipher) if x == word]
        if len(indices) == 1:
            answer += chr(cipher.index(word) + ord('A'))
            continue
        if len(indices) == 0:
            raise ValueError
        close.append(decrypt.index(word))
        close.append(indices)
        print(close, indices)
        answer += ' '
    except ValueError:
        close.append(difflib.get_close_matches(word, cipher))
        print(close)
        answer += ' '
    # indices = [i for i, x in enumerate(my_list) if x == "whatever"]
print("answer: " + answer)
p.sendline(answer)
decrypt = p.recv(timeout=5).decode("ascii").split("\n")[-2].split(" ")
if len(decrypt) == 1:
    decrypt = p.recv(timeout=5).decode("ascii").split("\n")[-2].split(" ")  
print(decrypt)
    
p.interactive()
