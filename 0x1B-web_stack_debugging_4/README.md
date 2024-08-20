# 0x1B. Web stack debugging #4
## Requirements
### General

- All your files will be interpreted on Ubuntu 14.04 LTS
- All your files should end with a new line
- A `README.md` file at the root of the folder of the project is mandatory
- Your Puppet manifests must pass `puppet-lint` version 2.1.1 without any errors
- Your Puppet manifests must run without error
- Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
- Your Puppet manifests files must end with the extension `.pp`
- Files will be checked with Puppet v3.4

Confirm Ubuntu version:
```sh

root@4e47757d8edd:/# lsb_release -a         
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 14.04.6 LTS
Release:        14.04
Codename:       trusty

```

#### Install puppet-lint

```sh
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```
Running the commands:
```sh
root@4e47757d8edd:/# sudo apt-get update
root@4e47757d8edd:/# apt-get install -y ruby
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ruby is already the newest version.
The following package was automatically installed and is no longer required:
  unzip
Use 'apt-get autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 7 not upgraded.
root@4e47757d8edd:/# gem install puppet-lint -v 2.1.1
Successfully installed puppet-lint-2.1.1
1 gem installed
Installing ri documentation for puppet-lint-2.1.1...
Installing RDoc documentation for puppet-lint-2.1.1...
root@4e47757d8edd:/# apt-get autoremove
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be REMOVED:
  unzip
0 upgraded, 0 newly installed, 1 to remove and 7 not upgraded.
After this operation, 395 kB disk space will be freed.
Do you want to continue? [Y/n] Y
(Reading database ... 28805 files and directories currently installed.)
Removing unzip (6.0-9ubuntu1.5) ...
Processing triggers for mime-support (3.54ubuntu1.1) ...
root@4e47757d8edd:/# sudo apt-get install apache2-utils

```

## Tasks
0. Sky is the limit, let's bring that limit higher

In this web stack debugging task, we are testing how well our web server setup featuring Nginx is doing under pressure and it turns out it’s not doing well: we are getting a huge amount of failed requests. <br />

For the benchmarking, we are using ApacheBench which is a quite popular tool in the industry. It allows you to simulate HTTP requests to a web server. In this case, I will make 2000 requests to my server with 100 requests at a time. We can see that 943 requests failed, let’s fix our stack so that we get to 0, and remember that when something is going wrong, logs are your best friends!

```sh

root@0a62aa706eb3:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   0.353 seconds
Complete requests:      2000
Failed requests:        943
   (Connect: 0, Receive: 0, Length: 943, Exceptions: 0)
Non-2xx responses:      1057
Total transferred:      1196526 bytes
HTML transferred:       789573 bytes
Requests per second:    5664.01 [#/sec] (mean)
Time per request:       17.655 [ms] (mean)
Time per request:       0.177 [ms] (mean, across all concurrent requests)
Transfer rate:          3309.15 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   1.1      0       8
Processing:     2   17   3.8     17      24
Waiting:        2   17   3.8     17      24
Total:          9   17   3.3     17      24

Percentage of the requests served within a certain time (ms)
  50%     17
  66%     19
  75%     20
  80%     20
  90%     21
  95%     23
  98%     23
  99%     23
 100%     24 (longest request)
root@0a62aa706eb3:/#
root@58f6b7cf89f4:/# sudo vim /etc/default/nginx 
root@58f6b7cf89f4:/# vi 0-the_sky_is_the_limit_not.pp
root@58f6b7cf89f4:/# puppet apply 0-the_sky_is_the_limit_not.pp
Notice: Compiled catalog for 58f6b7cf89f4.ec2.internal in environment production in 0.21 seconds
Notice: /Stage[main]/Main/Exec[Nginx-Update]/returns: executed successfully
Notice: /Stage[main]/Main/Exec[nginx-restart]/returns: executed successfully
Notice: Finished catalog run in 2.10 seconds
root@58f6b7cf89f4:/# sudo vi /etc/default/nginx 
root@58f6b7cf89f4:/# puppet apply 0-the_sky_is_the_limit_not.pp
Notice: Compiled catalog for 58f6b7cf89f4.ec2.internal in environment production in 0.21 seconds
Notice: /Stage[main]/Main/Exec[Nginx-Update]/returns: executed successfully
Notice: /Stage[main]/Main/Exec[nginx-restart]/returns: executed successfully
Notice: Finished catalog run in 2.10 seconds
root@58f6b7cf89f4:/# sudo vi /etc/default/nginx 
root@58f6b7cf89f4:/# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   2.741 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    729.62 [#/sec] (mean)
Time per request:       137.057 [ms] (mean)
Time per request:       1.371 [ms] (mean, across all concurrent requests)
Transfer rate:          607.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   34  48.0      2     187
Processing:     2   99  57.5     99     299
Waiting:        1   87  56.7     95     299
Total:          6  132  58.3    107     299

Percentage of the requests served within a certain time (ms)
  50%    107
  66%    186
  75%    192
  80%    193
  90%    198
  95%    203
  98%    289
  99%    291
 100%    299 (longest request)

```

File: `0-the_sky_is_the_limit_not.pp`

1. User limit
Change the OS configuration so that it is possible to login with the `holberton` user and open a file without any error message.
```sh

root@079b7269ec1b:~# su - holberton
-su: /etc/profile: Too many open files
-su: /home/holberton/.bash_profile: Too many open files
-su-4.3$ head /etc/passwd
-su: start_pipeline: pgrp pipe: Too many open files
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
-su-4.3$
-su-4.3$
-su-4.3$ logout
-su: /home/holberton/.bash_logout: Too many open files
-su: /etc/bash.bash_logout: Too many open files
root@079b7269ec1b:~#
root@079b7269ec1b:~#
root@68816e645300:/# vi 1-user_limit.pp
root@68816e645300:/# puppet apply 1-user_limit.pp 
Notice: Compiled catalog for 68816e645300.ec2.internal in environment production in 0.30 seconds
Notice: /Stage[main]/Main/Exec[Limit-increase-Hard]/returns: executed successfully
Notice: /Stage[main]/Main/Exec[Limit-increase-Soft]/returns: executed successfully
Notice: Finished catalog run in 1.20 seconds
root@079b7269ec1b:~#
root@079b7269ec1b:~#
root@079b7269ec1b:~# su - holberton
holberton@079b7269ec1b:~$ head /etc/passwd
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

```
Initially the secuity file `vi /etc/security/limits.conf`contains a limit of 5.
```sh

#Where:
#<domain> can be:
#        - a user name
#        - a group name, with @group syntax
#        - the wildcard *, for default entry
#        - the wildcard %, can be also used with %group syntax,
#                 for maxlogin limit
#        - NOTE: group and wildcard limits are not applied to root.
#          To apply a limit to the root user, <domain> must be
#          the literal username root.
#
#<type> can have the two values:
#        - "soft" for enforcing the soft limits
#        - "hard" for enforcing hard limits
#
#<item> can be one of the following:
#        - core - limits the core file size (KB)
#        - data - max data size (KB)
#        - fsize - maximum filesize (KB)
#        - memlock - max locked-in-memory address space (KB)
#        - nofile - max number of open files
#        - rss - max resident set size (KB)
#        - stack - max stack size (KB)
#        - cpu - max CPU time (MIN)
#        - nproc - max number of processes
#        - as - address space limit (KB)
#        - maxlogins - max number of logins for this user
#        - maxsyslogins - max number of logins on the system
#        - priority - the priority to run user process with
#        - locks - max number of file locks the user can hold
#        - sigpending - max number of pending signals
#        - msgqueue - max memory used by POSIX message queues (bytes)
#        - nice - max nice priority allowed to raise to values: [-20, 19]
#        - rtprio - max realtime priority
#        - chroot - change root to directory (Debian-specific)
#
#<domain>      <type>  <item>         <value>
#

#*               soft    core            0
#root            hard    core            100000
#*               hard    rss             10000
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
#ftp             -       chroot          /ftp
#@student        -       maxlogins       4

holberton hard nofile 5
holberton soft nofile 4
# End of file

```
After update, the limit is much higher:
```sh
...
#Where:
#<domain> can be:
#        - a user name
#        - a group name, with @group syntax
#        - the wildcard *, for default entry
#        - the wildcard %, can be also used with %group syntax,
#                 for maxlogin limit
#        - NOTE: group and wildcard limits are not applied to root.
#          To apply a limit to the root user, <domain> must be
#          the literal username root.
#
#<type> can have the two values:
#        - "soft" for enforcing the soft limits
#        - "hard" for enforcing hard limits
#
#<item> can be one of the following:
#        - core - limits the core file size (KB)
#        - data - max data size (KB)
#        - fsize - maximum filesize (KB)
#        - memlock - max locked-in-memory address space (KB)
#        - nofile - max number of open files
#        - rss - max resident set size (KB)
#        - stack - max stack size (KB)
#        - cpu - max CPU time (MIN)
#        - nproc - max number of processes
#        - as - address space limit (KB)
#        - maxlogins - max number of logins for this user
#        - maxsyslogins - max number of logins on the system
#        - priority - the priority to run user process with
#        - locks - max number of file locks the user can hold
#        - sigpending - max number of pending signals
#        - msgqueue - max memory used by POSIX message queues (bytes)
#        - nice - max nice priority allowed to raise to values: [-20, 19]
#        - rtprio - max realtime priority
#        - chroot - change root to directory (Debian-specific)
#
#<domain>      <type>  <item>         <value>
#

#*               soft    core            0
#root            hard    core            100000
#*               hard    rss             10000
#@student        hard    nproc           20
#@faculty        soft    nproc           20
#@faculty        hard    nproc           50
#ftp             hard    nproc           0
#ftp             -       chroot          /ftp
#@student        -       maxlogins       4

holberton hard nofile 10000
holberton soft nofile 20000
# End of file

```

File: `1-user_limit.pp`