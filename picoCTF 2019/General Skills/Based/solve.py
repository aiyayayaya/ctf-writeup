from pwn import *

with remote("2019shell1.picoctf.com", 29594) as conn:
    # Q1 - bin to ascii
    question = conn.recvuntil(b"Input:").split(b"\n")
    answer = ''.join([chr(int(i.decode(), 2)) for i in question[2].split(b" ")[3:-3]])
    # print(question, answer)
    conn.sendline(answer)

    # Q2 - dec to ascii
    question = conn.recvuntil(b"Input:").split(b"\n")
    answer = ''.join([chr(int(i.decode(), 8)) for i in question[1].split(b" ")[5:-3]])
    # print(question, answer)
    conn.sendline(answer)

    # Q3 - hex to ascii
    question = conn.recvuntil(b"Input:").split(b"\n")
    print(question)
    answer = bytearray.fromhex(question[1].split(b" ")[4].decode()).decode()
    # print(question, answer)
    conn.sendline(answer)

    conn.interactive()
    
