# [Day 1] Inventory Management

[Supporting materials](https://docs.google.com/document/d/1PHs7uRS1whLY9tgxH1lj-bnEVWtXPXpo45zWUlbknpU/edit?usp=sharing)

## Solution
The first step is to register a login. After setting up a random user, we have come to a page that ask for Christmas gifts requests. 

Now it is time to press F12 in chrome and inspect the cookies through  `Application -> Storage -> Cookies -> <Your ip>`. We can see there is a cookie with authid as its field name. So the first answer is authid. 

Next, we take a look at the authid value. It looks like it is url encoded. After decoding, it looks like it is a base64 encoded string. After we decode it again, we discovered that it is in the format of `<your user name>v4er9ll1!ss` and hence the second answer is v4er9ll1!ss.

Finally, we can login as mcinventory by encoding the string mcinventoryv4er9ll1!ss in base64 and url. We change the value of the cookie and successfully get the Christmas gift request: firewall. 