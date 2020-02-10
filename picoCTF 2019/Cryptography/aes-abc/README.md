# AES-ABC

## Question
AES-ECB is bad, so I rolled my own cipher block chaining mechanism - Addition Block Chaining! You can find the source here: aes-abc.py. The AES-ABC flag is body.enc.ppm

## Solution
The hint ask us to investigate into ECB mode. According to [this article](https://blog.filippo.io/the-ecb-penguin/), it seems like that if the image is encrypted with ECB mode, we can get the flag directly. 

Lets look at the python source code now. The source is isolating the header first, then divide the remaining image data into blocks and perform the following actions:
```python
prev_blk = int(blocks[i].encode('hex'), 16)
curr_blk = int(blocks[i+1].encode('hex'), 16)

n_curr_blk = (prev_blk + curr_blk) % UMAX
blocks[i+1] = to_bytes(n_curr_blk)
```
These few lines indicate that this is using cipher block chaining that xor-ed every block with the previous block. If we would like to get the original block, we can xor the current block with the previous block, starting from the last block. The script is in [solve.py](solve.py).

Flag: `picoCTF{d0Nt_r0ll_yoUr_0wN_aES}`