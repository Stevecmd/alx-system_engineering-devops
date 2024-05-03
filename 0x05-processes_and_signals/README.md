# 0x05. Processes and signals
## General

- What is a PID
- What is a process
- How to find a process’ PID
- How to kill a process
- What is a signal
- What are the 2 signals that cannot be ignored

## Requirements
### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.7.0` via `apt-get`) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what is the script doing

# Tasks
0. What is my PID
Write a Bash script that displays its own PID.


File: `0-what-is-my-pid`

1. List your processes 

Write a Bash script that displays a list of currently running processes.

Requirements:

- Must show all processes, for all users, including those which might not have a TTY
- Display in a user-oriented format
- Show process hierarchy

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root       704  0.0  0.0   7236  3980 pts/2    Ss   03:03   0:00 /bin/bash
root       760  0.0  0.0   6972  3428 pts/2    S+   03:13   0:00  \_ bash ./1-list_your_processes
root       762  0.0  0.0   9128  3456 pts/2    R+   03:13   0:00  |   \_ ps -auxf
root       761  0.0  0.0   5488   572 pts/2    S+   03:13   0:00  \_ head -50
root       134  0.0  0.0   7236  3956 pts/1    Ss   May01   0:00 /bin/bash
root       214  0.0  0.0  21852  9812 pts/1    S+   May01   0:00  \_ vi find3.py
root        22  0.0  0.0   7236  4012 pts/0    Ss+  Apr29   0:00 /bin/bash
root         1  0.0  0.0   6972  3312 ?        Ss   Apr29   0:00 /bin/bash /etc/sandbox_run.sh
root        17  0.0  0.0  12172  6956 ?        S    Apr29   0:00 sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups

```

File: `1-list_your_processes`

2. Show your Bash PID
Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

- You cannot use `pgrep`
- The third line of your script must be `# shellcheck disable=SC2009`

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./2-show_your_bash_pid 
root         1  0.0  0.0   6972  3312 ?        Ss   Apr29   0:00 /bin/bash /etc/sandbox_run.sh
root        22  0.0  0.0   7236  4012 pts/0    Ss+  Apr29   0:00 /bin/bash
root       134  0.0  0.0   7236  3956 pts/1    Ss   May01   0:00 /bin/bash
root       704  0.0  0.0   7236  3980 pts/2    Ss   03:03   0:00 /bin/bash
root       765  0.0  0.0   6972  3376 pts/2    S+   03:16   0:00 bash ./2-show_your_bash_pid
root       767  0.0  0.0   6300   724 pts/2    S+   03:16   0:00 grep bash

```

File: `2-show_your_bash_pid`

3. Show your Bash PID made easy 
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word `bash`.

Requirements:

- You cannot use `ps`

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./3-show_your_bash_pid_made_easy 
22 bash
134 bash
704 bash
770 bash
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./3-show_your_bash_pid_made_easy 
22 bash
134 bash
704 bash
772 bash

```

Here we can see that:

- For the first iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4555`
- For the second iteration: `bash` PID is `4404` and that the `3-show_your_bash_pid_made_easy` script PID is `4557`

File: `3-show_your_bash_pid_made_easy`

4. To infinity and beyond 
Write a Bash script that displays `To infinity and beyond` indefinitely.

Requirements:

- In between each iteration of the loop, add a `sleep 2`

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./4-to_infinity_and_beyond 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C

```

File: `4-to_infinity_and_beyond`

5. Don't stop me now! 

We stopped our `4-to_infinity_and_beyond` process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:

- You must use `kill`

Terminal #0

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./4-to_infinity_and_beyond 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond

```
Terminal #1
```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./5-dont_stop_me_now 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# 

```

File: `5-dont_stop_me_now`

6. Stop me if you can
Write a Bash script that stops `4-to_infinity_and_beyond` process.

Requirements:

- You cannot use `kill` or `killall`

Terminal #0

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./4-to_infinity_and_beyond 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated

```
Terminal #1

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./6-stop_me_if_you_can
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals#

```

File: `6-stop_me_if_you_can`

7. Highlander

Write a Bash script that displays:

- `To infinity and beyond` indefinitely
- With a `sleep 2` in between each iteration
- `I am invincible!!!` when receiving a `SIGTERM` signal

Make a copy of your `6-stop_me_if_you_can` script, name it `67-stop_me_if_you_can`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

Terminal #0
```sh
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
```

Terminal #1
```sh
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./67-stop_me_if_you_can 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./67-stop_me_if_you_can
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./67-stop_me_if_you_can
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# 
```


File: `7-highlander`

8. Beheaded process
Write a Bash script that kills the process `7-highlander`.

Terminal #0
```sh
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# 
```
Terminal #1
```sh
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# ./8-beheaded_process
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# 

```
File: `8-beheaded_process`

9. Process and PID file
Write a Bash script that:

- Creates the file `/var/run/myscript.pid` containing its PID
- Displays `To infinity and beyond` indefinitely
- Displays `I hate the kill command` when receiving a SIGTERM signal
- Displays `Y U no love me?`! when receiving a SIGINT signal
- Deletes the file `/var/run/myscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond

```
Executing the `100-process_and_pid_file` script and killing it with `ctrl+c`.

Terminal #0

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./100-process_and_pid_file
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
I hate the kill command

```
Terminal #1

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo pkill -f 100-process_and_pid_file

```
Starting `100-process_and_pid_file` in the terminal #0 and then killing it in the terminal #1.
File: `100-process_and_pid_file`

10. Manage my process

Programs that are detached from the terminal and running in the background are called daemons or processes, need to be managed. The general minimum set of instructions is: `start`, `restart` and `stop`. The most popular way of doing so on Unix system is to use the init scripts.

Write a `manage_my_process` Bash script that:

- Indefinitely writes `I am alive!` to the file `/tmp/my_process`
- In between every `I am alive!` message, the program should pause for 2 seconds

Write Bash (init) script `101-manage_my_process` that manages `manage_my_process`. (both files need to be pushed to git)

Requirements:

- When passing the argument `start`:
        - Starts `manage_my_process`
        - Creates a file containing its PID in /var/run/my_process.pid
        - Displays `manage_my_process` started
- When passing the argument stop:
        - Stops `manage_my_process`
        - Deletes the file /var/run/my_process.pid
        - Displays `manage_my_process` stopped
- When passing the argument restart
        - Stops `manage_my_process`
        - Deletes the file /var/run/my_process.pid
        - Starts `manage_my_process`
        - Creates a file containing its PID in /var/run/my_process.pid
        - Displays `manage_my_process` restarted
- Displays Usage: `manage_my_process` {start|stop|restart} if any other argument or no argument is passed

Note that this init script is far from being perfect (but good enough for the sake of manipulating process and PID file), for example we do not handle the case where we check if a process is already running when doing `./101-manage_my_process start`, in our case it will simply create a new process instead of saying that it is already started.

```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process
Usage: manage_my_process {start|stop|restart}
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process start
manage_my_process started
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
I am alive!
^C
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process stop
manage_my_process stopped
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# cat /var/run/my_process.pid 
cat: /var/run/my_process.pid: No such file or directory
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# tail -f -n0 /tmp/my_process 
^C
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process start
manage_my_process started
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# cat /var/run/my_process.pid 
11864
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process restart
manage_my_process restarted
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# cat /var/run/my_process.pid 
11918
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# tail -f -n0 /tmp/my_process 
I am alive!
I am alive!
I am alive!
^C

```

File: `101-manage_my_process, manage_my_process`

```sh
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process
Usage: manage_my_process {start|stop|restart}
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process start
manage_my_process started
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# tail -f -n0 /tmp/my_process 
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
^C
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process stop
manage_my_process stopped
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# cat /var/run/my_process.pid
cat: /var/run/my_process.pid: No such file or directory
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# tail -f -n0 /tmp/my_process
^C
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process start
manage_my_process started
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# cat /var/run/my_process.pid 
4278
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# sudo ./101-manage_my_process restart
manage_my_process restarted
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# cat /var/run/my_process.pid 
4320
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# tail -f -n0 /tmp/my_process 
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!
I am alive!
tail: /tmp/my_process: file truncated
I am alive!

```


### Shellcheck checks
```sh

root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 2-show_your_bash_pid 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 3-show_your_bash_pid_made_easy 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 4-to_infinity_and_beyond 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 5-dont_stop_me_now 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 6-stop_me_if_you_can 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 67-stop_me_if_you_can 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 7-highlander 
root@668e888f15e1:/alx-system_engineering-devops/0x05-processes_and_signals# shellcheck 8-beheaded_process 

```