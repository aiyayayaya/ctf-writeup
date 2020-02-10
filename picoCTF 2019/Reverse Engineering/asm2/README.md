# asm2

## Solution 
The given file:
```assembly
asm2:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	sub    esp,0x10
	<+6>:	mov    eax,DWORD PTR [ebp+0xc]          # move ebp+0xc to eax
	<+9>:	mov    DWORD PTR [ebp-0x4],eax          # move eax to ebp-0x4
	<+12>:	mov    eax,DWORD PTR [ebp+0x8]          # move ebp+0x8 to eax 
	<+15>:	mov    DWORD PTR [ebp-0x8],eax          # move eax to ebp-0x8
	<+18>:	jmp    0x50c <asm2+31>                  # jump to +31
	<+20>:	add    DWORD PTR [ebp-0x4],0x1          # ebp-0x4 + 1
	<+24>:	add    DWORD PTR [ebp-0x8],0xaf         # ebp-0x8 + 0xaf
	<+31>:	cmp    DWORD PTR [ebp-0x8],0xa3d3
	<+38>:	jle    0x501 <asm2+20>                  # if ebp-0x8 < 0xa3d3, jump to +20
	<+40>:	mov    eax,DWORD PTR [ebp-0x4]          # move ebp-0x4 to eax
	<+43>:	leave  
	<+44>:	ret    
```

The given argument are 0xc and 0x15. The program takes in 2 argument and check whether first argument is smaller than 0xa3d3. If yes, then it added 0x1 and 0xaf to the first and second argument respectively. This process is repeating until the condition is met. Hence, the flag is given by (0xa3d3 - 0xc) // 0xaf + 1 + 0x15. It is 0x105.