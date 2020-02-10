# like1000

## Question
This .tar file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c.

## Solution
The given file is a tarfile with "999.tar" and a "filler.txt" inside. Looks like this challenge wants us to unzip 1000 tar files. We can do this by using python:
```python
import tarfile
for i in range(1000, 0, -1):
    with tarfile.open(str(i) + '.tar', 'r') as zip_ref:
        zip_ref.extract(str(i-1) + '.tar', path='.')
```

The extraction stops at 1.tar. We can then extract the "flag.png" from it and get the flag.

Flag: `picoCTF{l0t5_0f_TAR5}`