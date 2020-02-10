# c0rrupt

## Question
We found this file. Recover the flag. You can also find the file in /problems/c0rrupt_0_1fcad1344c25a122a00721e4af86de13.

## Solution
The challenge asks us to fix the header of the file. Since the file is too large to be a normal text file with flag, image file would be a good guess. Let's take a look at the hex value:
```
00000000: 89 65 4E 34 0D 0A B0 AA 00 00 00 0D 43 22 44 52    .eN4..0*....C"DR
```

After googling the first few hex numbers, it looks like a PNG file. Since other image files do not share similarity with the hex values here, lets fix it assuming it is PNG.

After some research, PNG file comes with [IHDR](http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html#C.IHDR) block and IEND block. As we can find IEND block, we can confirm it is a PNG file. 

First, we need to fix the PNG header. Signature of PNG: `89 50 4E 47 0D 0A 1A 0A`, which is different from the first 8 bytes. After editting it with a hex editor, it becomes: 
`00000000: 89 50 4E 47 0D 0A 1A 0A 00 00 00 0D 49 48 44 52    .PNG........IHDR`

Next, we can use `pngcheck` to check the format.
```bash
user:~$ pngcheck mystery.png
mystery.png  CRC error in chunk pHYs (computed 38d82c82, expected 495224f0)
ERROR: mystery.png
```

How can we correct CRC? First, we need to know what is the structure of PNG files. Referring to [this specification](http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html), we summarize the following:

### Chunk layout
| Part | Size |
| ---- | ---- |
| Length | 4 bytes |
| Chunk Type | 4 bytes |
| Chunk Data | 0 or more bytes |
| CRC | 4 bytes 

### Chunk data sizes
gAMA: 4 bytes
sRGB: 1 byte
pHYs: 9 bytes
IHDR: 13 bytes

As such, we found that we need to change address `0x4f` to `0x52` for the CRC values. Still, it produces the following error:
```bash
user:~$ pngcheck mystery.png
mystery.png  invalid chunk length (too large)
ERROR: mystery.png
```

It did not specify what chunk it is. Hence, we need to refer to the following:

### Critical chunks (must appear in this order, except PLTE is optional):
| Name | Multiple OK? | Ordering constraints |
| ---- | ------------ | -------------------- |        
| IHDR | No |     Must be first |
| PLTE | No |    Before IDAT |
| IDAT |  Yes |    Multiple IDATs must be consecutive |
| IEND |   No  |    Must be last |
   
### Ancillary chunks (need not appear in this order):
| Name | Multiple OK? | Ordering constraints |
| ---- | ------------ | -------------------- |  
| cHRM  |  No  |    Before PLTE and IDAT |
| gAMA  |  No  |   Before PLTE and IDAT |
| iCCP  | No   |  Before PLTE and IDAT |
| sBIT |   No  |    Before PLTE and IDAT |
| sRGB  |  No     | Before PLTE and IDAT |
| bKGD  |  No    |  After PLTE; before IDAT |
| hIST  |  No   |   After PLTE; before IDAT |
| tRNS  |  No   |   After PLTE; before IDAT |
| pHYs  |  No   |   Before IDAT |
| sPLT  |  Yes  |   Before IDAT |
| tIME  |  No   |   None |
| iTXt  |  Yes  |   None |
| tEXt  |  Yes  |   None |
| zTXt  |  Yes  |   None |

It seems like that IDAT is the only part that looks like it as it is a long chunk of data. Now, we have to calculate the offset: `0xffff - 0x5a = 0xffa5` and hence the size is `0xffa5`.

Still, we need to fix the CRC.
```bash
user:~$ mystery.png  CRC error in chunk IDAT (computed e71ad68a, expected 6927db59)
ERROR: mystery.png
```

After changing the CRC, we produce a readable PNG file.

Flag: `picoCTF{c0rrupt10n_1847995}`