# asm3

## Question

## Solution
The given file
```assembly
asm3:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	xor    eax,eax                      # eax = 0
	<+5>:	mov    ah,BYTE PTR [ebp+0x9]        # move [ebp+0x9] to ah
	<+8>:	shl    ax,0x10                      # shift ax to the left by 2
	<+12>:	sub    al,BYTE PTR [ebp+0xd]        # al -= [ebp+0xd] 
	<+15>:	add    ah,BYTE PTR [ebp+0xe]        # ah += [ebp+0xe] 
	<+18>:	xor    ax,WORD PTR [ebp+0x12]       # ax ^= [ebp+0x12]
	<+22>:	nop
	<+23>:	pop    ebp
	<+24>:	ret    
```

The given arguments are 0xfe8cf7a4,0xf55018af,0xb8c70926. Thus, the stack looks like (note that it is little endian):
```
+---------------+
| old ebp       | <-- ebp
+---------------+
| ret           | <-- ebp + 0x4
+---------------+
| 0xfe8cf7a4    | <-- ebp + 0x8 (arg1)
+---------------+
| 0xf55018af    | <-- ebp + 0xc (arg2)
+---------------+
| 0xb8c70926    | <-- ebp + 0x10 (arg3)
+---------------+
```
Move [ebp+0x9](0xf7) to ah. (ax = 0xf700)

Shift ax to the left by 2. (ax = 0x0000)

al -= [ebp+0xd](0x18) (ax = 0x00e8)

ah += [ebp+0xe](0x50) (ax = 0x50e8)

ax ^= [ebp+0x12](0xb8c7) (ax = 0xe82f)