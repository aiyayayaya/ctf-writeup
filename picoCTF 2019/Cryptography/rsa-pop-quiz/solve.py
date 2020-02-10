from pwn import *

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    return x % m

with remote("2019shell1.picoctf.com", 30962) as conn:
    # Q1
    question = conn.recvuntil(b"(Y/N)")
    p, q = [int(i[4:].decode("ascii")) for i in question.split(b"\n")[-5:-3]]
    conn.send("Y\n" + str(p * q) + "\n")

    # Q2
    question = conn.recvuntil(b"(Y/N)")
    p, n = [int(i[4:].decode("ascii")) for i in question.split(b"\n")[-5:-3]]
    conn.send("Y\n" + str(n // p) + "\n")

    # Q3
    question = conn.recvuntil(b"(Y/N)")
    conn.send("N\n")

    # Q4
    question = conn.recvuntil(b"(Y/N)")
    p, q = [int(i[4:].decode("ascii")) for i in question.split(b"\n")[-5:-3]]
    conn.send("Y\n" + str((p - 1) * (q - 1)) + "\n")

    # Q5
    question = conn.recvuntil(b"(Y/N)")
    plaintext = int(question.split(b"\n")[-6][12:].decode("ascii"))
    e, n = [int(i[4:].decode("ascii")) for i in question.split(b"\n")[-5:-3]]
    conn.send("Y\n" + str(pow(plaintext, e, n)) + "\n")

    # Q6
    question = conn.recvuntil(b"(Y/N)")
    conn.send("N\n")

    # Q7
    question = conn.recvuntil(b"(Y/N)")
    q, p, e = [int(i[4:].decode("ascii")) for i in question.split(b"\n")[-6:-3]]
    conn.send("Y\n" + str(modinv(e, (p-1)*(q-1))) + "\n")

    # Q8
    question = conn.recvuntil(b"(Y/N)")
    p = int(question.split(b"\n")[-7][4:].decode("ascii"))
    ciphertext = int(question.split(b"\n")[-6][13:].decode("ascii"))
    e, n = [int(i[4:].decode("ascii")) for i in question.split(b"\n")[-5:-3]]
    q = n // p
    plaintext = pow(ciphertext, modinv(e, (p-1)*(q-1)), n)
    conn.send("Y\n" + str(plaintext) + "\n")
    
    print(bytearray.fromhex(hex(plaintext)[2:]).decode())