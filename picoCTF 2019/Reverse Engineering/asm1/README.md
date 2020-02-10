# asm1

## Question
What does asm1(0x345) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/asm1_5_301df039c0ee4ee4dfa8adad6a40b875.

## Solution
The file given to us is as follow:
```assembly
asm1:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	cmp    DWORD PTR [ebp+0x8],0x37a            
	<+10>:	jg     0x512 <asm1+37>                      # if first function argument > 0x37a, jump to +37 if 
	<+12>:	cmp    DWORD PTR [ebp+0x8],0x345
	<+19>:	jne    0x50a <asm1+29>                      # if first function argument != -x345, jump to +29
	<+21>:	mov    eax,DWORD PTR [ebp+0x8]
	<+24>:	add    eax,0x3
	<+27>:	jmp    0x529 <asm1+60>
	<+29>:	mov    eax,DWORD PTR [ebp+0x8]
	<+32>:	sub    eax,0x3
	<+35>:	jmp    0x529 <asm1+60>
	<+37>:	cmp    DWORD PTR [ebp+0x8],0x5ff
	<+44>:	jne    0x523 <asm1+54>
	<+46>:	mov    eax,DWORD PTR [ebp+0x8]
	<+49>:	sub    eax,0x3
	<+52>:	jmp    0x529 <asm1+60>
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]
	<+57>:	add    eax,0x3
	<+60>:	pop    ebp
	<+61>:	ret    
```
The program argument is 0x345, so it is not greater than 0x37a and it would execute +21 and add 3 to 0x345. It then jump to +60 and return the argument. Hence the answer is 0x348.