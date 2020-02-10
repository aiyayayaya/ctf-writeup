# asm4

## Question
What will asm4("picoCTF_fdb55") return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source located in the directory at /problems/asm4_0_95e4374e96bc98228a50a6b8e3e41483.

## Solution
The given file is as following:
```assembly
asm4:
	<+0>:	push   ebp
	<+1>:	mov    ebp,esp
	<+3>:	push   ebx
	<+4>:	sub    esp,0x10
	<+7>:	mov    DWORD PTR [ebp-0x10],0x260           # ebp-0x10 = 0x260
	<+14>:	mov    DWORD PTR [ebp-0xc],0x0              # ebp-0xc = 0
	<+21>:	jmp    0x518 <asm4+27>                      # jump to +27
	<+23>:	add    DWORD PTR [ebp-0xc],0x1              # ebp-0xc += 1
	<+27>:	mov    edx,DWORD PTR [ebp-0xc]              
	<+30>:	mov    eax,DWORD PTR [ebp+0x8]              
	<+33>:	add    eax,edx                              # eax = ebp-0xc + ebp+0x8
	<+35>:	movzx  eax,BYTE PTR [eax]                   # eax = eax (with zero extend)
	<+38>:	test   al,al
	<+40>:	jne    0x514 <asm4+23>                      # if al != 0, jump to +23
	<+42>:	mov    DWORD PTR [ebp-0x8],0x1              # ebp-0x8 = 1
	<+49>:	jmp    0x587 <asm4+138>                     # jump to +138
	<+51>:	mov    edx,DWORD PTR [ebp-0x8]              
	<+54>:	mov    eax,DWORD PTR [ebp+0x8]              
	<+57>:	add    eax,edx                              # edx = ebp-0x8 + ebp+0x8
	<+59>:	movzx  eax,BYTE PTR [eax]                   # eax = eax(zero extend)
	<+62>:	movsx  edx,al                               # edx = al (sign extend)
	<+65>:	mov    eax,DWORD PTR [ebp-0x8]              # ebp-0x8 = eax 
	<+68>:	lea    ecx,[eax-0x1]                        
	<+71>:	mov    eax,DWORD PTR [ebp+0x8]              
	<+74>:	add    eax,ecx                              # eax = ebp+0x8 + *ebp-0x1
	<+76>:	movzx  eax,BYTE PTR [eax]                   # eax = eax (zero extend)
	<+79>:	movsx  eax,al                               # al = eax (sign extend)
	<+82>:	sub    edx,eax                              # edx -= eax
	<+84>:	mov    eax,edx                              # eax = ebx
	<+86>:	mov    edx,eax                              # edx = eax
	<+88>:	mov    eax,DWORD PTR [ebp-0x10]             # eax = ebp-0x10
	<+91>:	lea    ebx,[edx+eax*1]                      # ebx = edx+eax
	<+94>:	mov    eax,DWORD PTR [ebp-0x8]              
	<+97>:	lea    edx,[eax+0x1]                        
	<+100>:	mov    eax,DWORD PTR [ebp+0x8]              
	<+103>:	add    eax,edx                              # eax = ebp+0x8 + *(ebp-0x8 + 1)
	<+105>:	movzx  eax,BYTE PTR [eax]                   # eax = eax(zero extend)
	<+108>:	movsx  edx,al                               # al = edx (sign extend)
	<+111>:	mov    ecx,DWORD PTR [ebp-0x8]              # move ebp-0x8 = ecx
	<+114>:	mov    eax,DWORD PTR [ebp+0x8]              # ebp+0x8 = eax
	<+117>:	add    eax,ecx                              # ecx += eax
	<+119>:	movzx  eax,BYTE PTR [eax]                   # eax = eax (zero extend)
	<+122>:	movsx  eax,al                               # al = eax (sign extend)
	<+125>:	sub    edx,eax                              # eax -= edx
	<+127>:	mov    eax,edx                              # edx = eaex
	<+129>:	add    eax,ebx                              # eax = ebx + eax
	<+131>:	mov    DWORD PTR [ebp-0x10],eax             # ebp-0x10 = eax
	<+134>:	add    DWORD PTR [ebp-0x8],0x1              # ebp-0x8 += 0x1
	<+138>:	mov    eax,DWORD PTR [ebp-0xc]              
	<+141>:	sub    eax,0x1                              
	<+144>:	cmp    DWORD PTR [ebp-0x8],eax              
	<+147>:	jl     0x530 <asm4+51>                      # if ebp-0x8 < ebp-0xc - 1, jump to +51
	<+149>:	mov    eax,DWORD PTR [ebp-0x10]             # eax = ebp-0x10
	<+152>:	add    esp,0x10                             
	<+155>:	pop    ebx
	<+156>:	pop    ebp
	<+157>:	ret    
```
