## Web exploitation

### Dirsearch

From tryhackme:
An example of running this tool shows:
./dirsearch.py -u https://www.tryhackme.com/ -w ./DirBuster-Lists/directory-list-2.3-big.txt -e html

Syntax:
-u is the hostname of the website
-w is the wordlist
-e is the extension:
Different web pages use different technologies(you can usually identify this by the file it loads in the browser e.g. if it’s a .js, .aspx page)
-f is the flag used to force extensions applied to the pages in the word list:
Mostly used when you’re quite sure about what kind of technology a server is running
If you don’t know what extension to brute force, you don’t need to specify this flag

### Hydra

#### FTP
`hydra -l user -P passlist.txt ftp://192.168.0.1`

#### SSH
`hydra -l <username> -P <full path to pass> <ip> -t 4 ssh`

-l is for the username
-P Hydra to use a list of passwords, we can also pass in a list of usernames to try in combination with the password list using -L.
-t specifies the number of threads used

#### Web form
##### Post
`hydra -l <username> -P <password list> <ip> http-post-form "/<login url>:username=^USER^&password=^PASS^:F=incorrect" -V`

| OPTION	| DESCRIPTION |
| --------- | ----------- |
| -l	| Single username |
| -P	| indicates use the following password list |
| http-post-form	| indicates the type of form (post) |
| /login url	| the login page URL |
| :username	| the form field where the username is entered |
| ^USER^	| tells Hydra to use the username |
| password	| the form field where the password is entered |
| ^PASS^	| tells Hydra to use the password list supplied earlier |
| Login	| indicates to Hydra the Login failed message |
| Login failed	| is the login failure message that the form returns |
| F=incorrect	| If this word appears on the page, its incorrect |
| -V	| verborse output for every attempt |

### SQLMap
Example:
`python3 sqlmap.py -u http://<ip>/register.php --risk=3 --level=5 --batch --dbms=mysql -p <field> -D <db name> --forms -T <table name> --dump`
| OPTION | DESCRIPTION |
| ------ | ----------- |
| -h | Show basic help message and exit |
| -u URL, --url=URL | Target URL (e.g. "http://www.site.com/vuln.php?id=1") |
| --dbms=DBMS | Force back-end DBMS to provided value |
| -p TESTPARAMETER | Testable parameter(s)|
| --current-user |Retrieve DBMS current user |
| --current-db | Retrieve DBMS current database |
| --passwords       | Enumerate DBMS users password hashes |
| --tables          | Enumerate DBMS database tables |
| --columns         | Enumerate DBMS database table columns |
| --schema          | Enumerate DBMS schema |
| --dump            | Dump DBMS database table entries |
| --dump-all        | Dump all DBMS databases tables entries |
| -D DB             | DBMS database to enumerate |
| -T TBL           | DBMS database table(s) to enumerate |
| -C COL            | DBMS database table column(s) to enumerate |

## Cryptography

### Hashcat
`hashcat64 -m <hash type> <hash> rockyou.txt --show`
[list of hash types](https://hashcat.net/wiki/doku.php?id=example_hashes)
Important ones:
- 0 - MD5
- 1800 - sha512crypt \$6\$, SHA512 (Unix)

### Notes on RSA
n = pq
totient(n) = (p-1)(q-1)
c = m^e mod n
m = c^d mod n

## Reverse Engineering/ Binary Exploitation

### Registers
<table>
  <tr>
    <td align='center'>32-bit</td>
    <td align='center' colspan="4">eax</td>
    <td align='center' colspan="4">ebx</td>
    <td align='center' colspan="4">ecx</td>
    <td align='center' colspan="4">edx</td>
  </tr>
  <tr>
    <td align='center'>16-bit</td>
    <td align='center' colspan="2"></td>
    <td align='center' colspan="2">ax</td>
    <td align='center' colspan="2"></td>
    <td align='center' colspan="2">bx</td>
    <td align='center' colspan="2"></td>
    <td align='center' colspan="2">cx</td>
    <td align='center' colspan="2"></td>
    <td align='center' colspan="2">dx</td>
  </tr>
  <tr>
    <td align='center'>8-bit</td>
    <td align='center'></td>
    <td align='center'></td>
    <td align='center'>ah</td>
    <td align='center'>al</td>
    <td align='center'></td>
    <td align='center'></td>
    <td align='center'>bh</td>
    <td align='center'>bl</td>
    <td align='center'></td>
    <td align='center'></td>
    <td align='center'>ch</td>
    <td align='center'>cl</td>
    <td align='center'></td>
    <td align='center'></td>
    <td align='center'>dh</td>
    <td align='center'>dl</td>
  </tr>
</table>


<table>
    <tr>
        <td align='center'>32-bit</td>
        <td align='center' colspan="2">esi</td>
        <td align='center' colspan="2">edi</td>
        <td align='center' colspan="2">ebp</td>
        <td align='center' colspan="2">esp</td>
    </tr>
    <tr>
        <td align='center'>16-bit</td>
        <td align='center'></td>
        <td align='center'>si</td>
        <td align='center'></td>
        <td align='center'>di</td>
        <td align='center'></td>
        <td align='center'>bp</td>
        <td align='center'></td>
        <td align='center'>sp</td>
    </tr>
</table>

### Shellcode
In python pwntools: `asm(shellcraft.i386.linux.sh())` - execute /bin/bash as root