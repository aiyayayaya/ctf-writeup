# [Day 2] Arctic Forum

[supporting material](https://docs.google.com/document/d/1622ejYtCmLOS0zd16CyfhA1xgQk8l55gYWMY8fnpHfQ/edit?usp=sharing)

## Solution
As the supporting material suggests, lets use dirsearch to search for hidden paths. We type `./dirsearch.py -u 10.10.99.80:3000 -w ./DirBuster-Lists/directory-list-2.3-medium.txt -e html` and wait... Bingo, we got `/sysadmin`!

Next, we go to the `/sysadmin` page and inspect the source code. We saw the comment `Admin portal created by arctic digital design`. Lets search `arctic digital design` on github. We found one repository [link](https://github.com/ashu-savani/arctic-digital-design) so we know the password is defaultpass.

Finally, we use the given credentials to login and get the final answer: Eggnog.