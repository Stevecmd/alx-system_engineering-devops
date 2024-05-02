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