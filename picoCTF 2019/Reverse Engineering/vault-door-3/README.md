# vault-door-3


## Question
This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java


## Solution
The given program:
```java
import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm16g84c_u_4_m0r846");
    }
}
```
We need to reverse the procedure in checkPassword:
```python
>>> a = 'jU5t_a_sna_3lpm16g84c_u_4_m0r846'
>>> b = [''] * 32
>>> for i in range(8):
...     b[i] = a[i]
...
>>> for i in range(8, 16):
...     b[i] = a[23-i]
...
>>> for i in range(16, 32, 2):
...     b[i] = a[46-i]
...
>>> for i in range(31, 16, -2):
...     b[i] = a[i]
...
>>> ''.join(b)
'jU5t_a_s1mpl3_an4gr4m_4_u_c08866'
```
flag: `picoCTF{jU5t_a_s1mpl3_an4gr4m_4_u_c08866}`