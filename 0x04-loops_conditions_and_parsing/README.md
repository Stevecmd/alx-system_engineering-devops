# 0x04. Loops, conditions and parsing

### General

- How to create SSH keys
- What is the advantage of using `#!/usr/bin/env bash` over `#!/bin/bash`
- How to use `while`, `until` and `for` loops
- How to use if, `else`, `elif` and `case` condition statements
- How to use the `cut` command
- What are files and other comparison operators, and how to use them

## Requirements
### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- You are not allowed to use `awk`
- Your Bash script must pass `Shellcheck` (version `0.7.0`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Shellcheck

[Shellcheck](https://github.com/koalaman/shellcheck) is a tool that will help you write proper Bash scripts. It will make recommendations on your syntax and semantics and provide advice on edge cases that you might not have thought about. Shellcheck is your friend! All your Bash scripts must pass Shellcheck without any error or you will not get any points on the task.

## Testing Shellcheck
Create bad_script and insert the code below:
```sh

#!/usr/bin/env bash
var='some text'
unused_variable='sme unused variable'

echo $var

```

Create good_script and insert the code below:
```sh

#!/usr/bin/env bash
var='some text'
unused_variable='sme unused variable'

echo "$var"
echo "$unused_variable"

```
Install shell check:
```sh

stevecmd@DESKTOP-UTB295U:~/alx-system_engineering-devops$ sudo apt install shellcheck
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following NEW packages will be installed:
  shellcheck
0 upgraded, 1 newly installed, 0 to remove and 33 not upgraded.
Need to get 2359 kB of archives.
After this operation, 16.3 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu jammy/universe amd64 shellcheck amd64 0.8.0-2 [2359 kB]
Fetched 2359 kB in 3s (777 kB/s)      
Selecting previously unselected package shellcheck.
(Reading database ... 32895 files and directories currently installed.)
Preparing to unpack .../shellcheck_0.8.0-2_amd64.deb ...
Unpacking shellcheck (0.8.0-2) ...
Setting up shellcheck (0.8.0-2) ...
Processing triggers for man-db (2.10.2-1) ...
```

Run shell check and expect the output below:
```sh

stevecmd@DESKTOP-UTB295U:~/alx-system_engineering-devops$ cd 0x04-loops_conditions_and_parsing/
stevecmd@DESKTOP-UTB295U:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ shellcheck bad_script

In bad_script line 3:
unused_variable='sme unused variable'
^-------------^ SC2034 (warning): unused_variable appears unused. Verify use (or export if used externally).


In bad_script line 5:
echo $var
     ^--^ SC2086 (info): Double quote to prevent globbing and word splitting.

Did you mean: 
echo "$var"

For more information:
  https://www.shellcheck.net/wiki/SC2034 -- unused_variable appears unused. V...
  https://www.shellcheck.net/wiki/SC2086 -- Double quote to prevent globbing ...
stevecmd@DESKTOP-UTB295U:~/alx-system_engineering-devops/0x04-loops_conditions_and_parsing$ shellcheck good_script

```
## Tasks

0. Create a SSH RSA key pair
Instructions. </ br>
[Windows users](https://docs.rackspace.com/docs/generating-rsa-keys-with-ssh-puttygen)

File: `0-RSA_public_key.pub`

1. For Best School loop
Write a Bash script that displays `Best School` 10 times.

Requirement:

- You must use the `for` loop (`while` and `until` are forbidden)
```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# head -n 2 1-for_best_school 
#!/usr/bin/env bash
# This script is displaying "Best School" 10 times
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./1-for_best_school 
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School

```
File: `1-for_best_school`

2. While Best School loop
Write a Bash script that displays `Best School` 10 times.

Requirements:

- You must use the `while` loop (`for` and `until` are forbidden)
```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./2-while_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School

```

File: `2-while_best_school`


3. Until Best School loop
Write a Bash script that displays `Best School` 10 times.

Requirements:

- You must use the until loop (`for` and `while` are forbidden)

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./3-until_best_school
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School

```
File: `3-until_best_school`

4. If 9, say Hi!
Write a Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line.

Requirements:

- You must use the `while` loop (`for` and `until` are forbidden)
- You must use the `if` statement

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./4-if_9_say_hi
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Best School
Hi
Best School

```
File: `4-if_9_say_hi`

5. 4 bad luck, 8 is your chance
Write a Bash script that loops from 1 to 10 and:

- displays `bad luck` for the 4th loop iteration
- displays `good luck` for the 8th loop iteration
- displays `Best School` for the other iterations

Requirements:

- You must use the `while` loop (for and until are forbidden)
- You must use the `if`, `elif` and `else` statements

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./5-4_bad_luck_8_is_your_chance
Best School
Best School
Best School
bad luck
Best School
Best School
Best School
good luck
Best School
Best School

```

File: `5-4_bad_luck_8_is_your_chance`

6. Superstitious numbers
Write a Bash script that displays numbers from 1 to 20 and:

- displays `4` and then `bad luck from China` for the 4th loop iteration
- displays `9` and then `bad luck from Japan` for the 9th loop iteration
- displays `17` and then `bad luck from Italy` for the 17th loop iteration

Requirements:

- You must use the `while` loop (for and until are forbidden)
- You must use the `case` statement

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./6-superstitious_numbers
1
2
3
4
bad luck from China
5
6
7
8
9
bad luck from Japan
10
11
12
13
14
15
16
17
bad luck from Italy
18
19
20

```
File: `6-superstitious_numbers`

7. Clock 

Write a Bash script that displays the time for 12 hours and 59 minutes:

- display hours from 0 to 12
- display minutes from 1 to 59

Requirements:

- You must use the `while` loop (`for` and un`til are forbidden)

Note that in this example, we only display the first 70 lines using the `head` command.

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./7-clock | head -n 70
Hour: 0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
Hour: 1
1
2
3
4
5
6
7
8
9

```

File: `7-clock`

8. For ls

Write a Bash script that displays:

- The content of the current directory
- In a list format
- Where only the part of the name after the first dash is displayed (refer to the example)

Requirements:

- You must use the `for` loop (`while` and `until` are forbidden)
- Do not display hidden files

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ls
0-RSA_public_key.pub  1-for_best_school    4-if_9_say_hi                  7-clock                   bad_script
100-read_and_cut      2-while_best_school  5-4_bad_luck_8_is_your_chance  8-for_ls                  good_script
10-fizzbuzz           3-until_best_school  6-superstitious_numbers        9-to_file_or_not_to_file  README.md
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./8-for_ls
RSA_public_key.pub
read_and_cut
fizzbuzz
for_best_school
while_best_school
until_best_school
if_9_say_hi
4_bad_luck_8_is_your_chance
superstitious_numbers
clock
for_ls
to_file_or_not_to_file
bad_script
good_script
README.md

```

File: `8-for_ls`

9. To file, or not to file
Write a Bash script that gives you information about the `school` file.

Requirements:

- You must use `if` and, `else` (`case` is forbidden)
- Your Bash script should check if the file exists and print:

        - if the file exists: `school file exists`
        - if the file does not exist: `school file does not exist`
- If the file exists, print:

        - if the file is empty: `school file is empty`
        - if the file is not empty: `school file is not empty`
        - if the file is a regular file: `school is a regular file`
        - if the file is not a regular file: (nothing)

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# file school
school: cannot open `school' (No such file or directory)
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./9-to_file_or_not_to_file 
school file does not exist
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# touch school
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./9-to_file_or_not_to_file 
school file exists
school file is empty
school is a regular file
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# echo 'betty' > school
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./9-to_file_or_not_to_file 
school file exists
school file is not empty
school is a regular file
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# rm school
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# mkdir school
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./9-to_file_or_not_to_file
school file exists
school file is not empty

```
File: `9-to_file_or_not_to_file`

10. FizzBuzz
Write a Bash script that displays numbers from 1 to 100.

Requirements:

- Displays `FizzBuzz` when the number is a multiple of 3 and 5
- Displays `Fizz` when the number is multiple of 3
- Displays `Buzz` when the number is a multiple of 5
- Otherwise, displays the number
- In a list format

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./10-fizzbuzz | head -20
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz

```
File: `10-fizzbuzz`

11. Read and cut
Write a Bash script that displays the content of the file `/etc/passwd`.

Your script should only display:

- username
- user id
- Home directory path for the user

Requirements:

- You must use the `while` loop (`for` and `until` are forbidden)

```sh
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:101:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:105::/nonexistent:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
mysql:x:106:107:MySQL Server,,,:/var/lib/mysql/:/bin/false

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# chmod u+x 100-read_and_cut
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./100-read_and_cut
root:0:/root
daemon:1:/usr/sbin
bin:2:/bin
sys:3:/dev
sync:4:/bin
games:5:/usr/games
man:6:/var/cache/man
lp:7:/var/spool/lpd
mail:8:/var/mail
news:9:/var/spool/news
uucp:10:/var/spool/uucp
proxy:13:/bin
www-data:33:/var/www
backup:34:/var/backups
list:38:/var/list
irc:39:/var/run/ircd
gnats:41:/var/lib/gnats
nobody:65534:/nonexistent
_apt:100:/nonexistent
systemd-timesync:101:/run/systemd
systemd-network:102:/run/systemd
systemd-resolve:103:/run/systemd
messagebus:104:/nonexistent
sshd:105:/run/sshd
mysql:106:/var/lib/mysql/

```
File: `100-read_and_cut`

12. Tell the story of passwd
The file `/etc/passwd` has already been covered in a `previous project` and you should be familiar with it. Today we will make up a story based on it.

Write a Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS.

Format: `The user USERNAME is part of the GROUP_ID gang, lives in HOME_DIRECTORY and rides COMMAND/SHELL. USER ID's place is protected by the passcode PASSWORD, more info about the user here: USER ID INFO`

Requirements:

- You must use the `while` loop (`for` and `until` are forbidden)


```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 101-tell_the_story_of_passwd
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./101-tell_the_story_of_passwd

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./101-tell_the_story_of_passwd
The user root is part of the 0 gang, lives in /root and rides /bin/bash. 0's place is protected by the passcode x, more info about the user here: root
The user daemon is part of the 1 gang, lives in /usr/sbin and rides /usr/sbin/nologin. 1's place is protected by the passcode x, more info about the user here: daemon
The user bin is part of the 2 gang, lives in /bin and rides /usr/sbin/nologin. 2's place is protected by the passcode x, more info about the user here: bin
The user sys is part of the 3 gang, lives in /dev and rides /usr/sbin/nologin. 3's place is protected by the passcode x, more info about the user here: sys
The user sync is part of the 65534 gang, lives in /bin and rides /bin/sync. 4's place is protected by the passcode x, more info about the user here: sync
The user games is part of the 60 gang, lives in /usr/games and rides /usr/sbin/nologin. 5's place is protected by the passcode x, more info about the user here: games
The user man is part of the 12 gang, lives in /var/cache/man and rides /usr/sbin/nologin. 6's place is protected by the passcode x, more info about the user here: man
The user lp is part of the 7 gang, lives in /var/spool/lpd and rides /usr/sbin/nologin. 7's place is protected by the passcode x, more info about the user here: lp
The user mail is part of the 8 gang, lives in /var/mail and rides /usr/sbin/nologin. 8's place is protected by the passcode x, more info about the user here: mail
The user news is part of the 9 gang, lives in /var/spool/news and rides /usr/sbin/nologin. 9's place is protected by the passcode x, more info about the user here: news
The user uucp is part of the 10 gang, lives in /var/spool/uucp and rides /usr/sbin/nologin. 10's place is protected by the passcode x, more info about the user here: uucp
The user proxy is part of the 13 gang, lives in /bin and rides /usr/sbin/nologin. 13's place is protected by the passcode x, more info about the user here: proxy
The user www-data is part of the 33 gang, lives in /var/www and rides /usr/sbin/nologin. 33's place is protected by the passcode x, more info about the user here: www-data
The user backup is part of the 34 gang, lives in /var/backups and rides /usr/sbin/nologin. 34's place is protected by the passcode x, more info about the user here: backup
The user list is part of the 38 gang, lives in /var/list and rides /usr/sbin/nologin. 38's place is protected by the passcode x, more info about the user here: Mailing List Manager
The user irc is part of the 39 gang, lives in /var/run/ircd and rides /usr/sbin/nologin. 39's place is protected by the passcode x, more info about the user here: ircd
The user gnats is part of the 41 gang, lives in /var/lib/gnats and rides /usr/sbin/nologin. 41's place is protected by the passcode x, more info about the user here: Gnats Bug-Reporting System (admin)
The user nobody is part of the 65534 gang, lives in /nonexistent and rides /usr/sbin/nologin. 65534's place is protected by the passcode x, more info about the user here: nobody
The user _apt is part of the 65534 gang, lives in /nonexistent and rides /usr/sbin/nologin. 100's place is protected by the passcode x, more info about the user here: 
The user systemd-timesync is part of the 101 gang, lives in /run/systemd and rides /usr/sbin/nologin. 101's place is protected by the passcode x, more info about the user here: systemd Time Synchronization,,,
The user systemd-network is part of the 103 gang, lives in /run/systemd and rides /usr/sbin/nologin. 102's place is protected by the passcode x, more info about the user here: systemd Network Management,,,
The user systemd-resolve is part of the 104 gang, lives in /run/systemd and rides /usr/sbin/nologin. 103's place is protected by the passcode x, more info about the user here: systemd Resolver,,,
The user messagebus is part of the 105 gang, lives in /nonexistent and rides /usr/sbin/nologin. 104's place is protected by the passcode x, more info about the user here: 
The user sshd is part of the 65534 gang, lives in /run/sshd and rides /usr/sbin/nologin. 105's place is protected by the passcode x, more info about the user here: 
The user mysql is part of the 107 gang, lives in /var/lib/mysql/ and rides /bin/false. 106's place is protected by the passcode x, more info about the user here: MySQL Server,,,

```
File: `101-tell_the_story_of_passwd`

13. Let's parse Apache logs
Write a Bash script that displays the visitor IP along with the `HTTP status code` from the Apache log file.

Requirement:

- Format: IP HTTP_CODE
       -in a list format
       -See example
- You must use awk
- You are not allowed to use `while`, `for`, `until` and `cut`

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# ./102-lets_parse_apache_logs | tail -n 10
185.130.5.207 301
185.130.5.207 301
91.224.140.223 200
62.210.142.23 304
92.222.20.166 304
180.76.15.19 200
2.1.201.36 304
198.58.99.82 304
50.116.30.23 304
209.133.111.211 200

```
File: `102-lets_parse_apache_logs`



### Shell-Check mandatory tasks
Combined shell check for mandatory tasks:
```sh

root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 1-for_best_school 
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 2-while_best_school
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 3-until_best_school 
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 4-if_9_say_hi
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 5-4_bad_luck_8_is_your_chance
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 6-superstitious_numbers 
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 7-clock
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 8-for_ls 
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 9-to_file_or_not_to_file
root@668e888f15e1:/alx-system_engineering-devops/0x04-loops_conditions_and_parsing# shellcheck 10-fizzbuzz 

```