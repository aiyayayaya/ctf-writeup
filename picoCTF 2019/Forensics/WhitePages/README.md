# WhitePages

## Question
I stopped using YellowPages and moved onto WhitePages... but the page they gave me is all blank!

## Solution
The file given to us looks like it is blank. However, the contents are full of tabs and other whitespaces. Lets use python to figure this out.

```python
with open('whitepages.txt', 'r') as f:
    contents = f.read()
splitted = [i for i in contents]
print(set(splitted))
```
Output: `{'\u2003', ' '}`

It looks like these two character represents a binary code. Lets try to decode it as ASCII:
```python
binary = ['1' if i == ' ' else '0' for i in splitted]
combined_bytes = [''.join(binary[i:i+8]) for i in range(0, len(binary), 8)]
print(''.join([chr(int(i, 2)) for i in bytes]))
```
Output: `'\n\t\tpicoCTF\n\n\t\tSEE PUBLIC RECORDS & BACKGROUND REPORT\n\t\t5000 Forbes Ave, Pittsburgh, PA 15213\n\t\tpicoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}\n\t\t'`

Flag: `picoCTF{not_all_spaces_are_created_equal_dd5c2e2f77f89f3051c82bfee7d996ef}`