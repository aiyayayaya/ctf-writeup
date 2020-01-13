# Dirsearch

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
