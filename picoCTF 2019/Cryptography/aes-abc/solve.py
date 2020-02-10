import tqdm
import math

BLOCK_SIZE = 16
results = []
UMAX = int(math.pow(256, BLOCK_SIZE))

with open('body.enc.ppm', 'rb') as f:
    content = f.read().split(b"\n")
    header, pixels = b"\n".join(content[:3]), b"\n".join(content[3:])
    blocks = [pixels[i * BLOCK_SIZE:(i+1) * BLOCK_SIZE] for i in range(len(pixels) // BLOCK_SIZE)]
    prev_blk = 0
    for i in blocks:
        curr_blk = int.from_bytes(i, "little")
        n_curr_blk = (curr_blk - prev_blk) %UMAX
        results.append(n_curr_blk) 
        prev_blk = curr_blk
    # print(blocks)
print(header)
with open('body.ppm', 'wb') as fw:
    fw.write(header)
    for i in tqdm.tqdm(results):
        fw.write(i.to_bytes(16, 'little'))