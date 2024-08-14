# 0x17-web_stack_debugging_3

### Resources
[Puppet-Lint](http://puppet-lint.com/) <br />
[Puppet-CookBook](https://www.puppetcookbook.com/posts/install-and-run-puppet-lint.html)

### Install puppet-lint
```sh
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```

## Tasks
0. Strace is your friend

Using strace, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using Puppet (instead of using Bash as you were previously doing).

Hint:

- `strace` can attach to a current running process
- You can use `tmux` to run `strace` in one window and `curl` in another one

Requirements:

- Your `0-strace_is_your_friend.pp` file must contain Puppet code
- You can use whatever Puppet resource type you want for you fix

Example:
```sh

root@e514b399d69d:~# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@e514b399d69d:~# puppet apply 0-strace_is_your_friend.pp
Notice: Compiled catalog for e514b399d69d.ec2.internal in environment production in 0.02 seconds
Notice: /Stage[main]/Main/Exec[fix-wordpress]/returns: executed successfully
Notice: Finished catalog run in 0.08 seconds
root@e514b399d69d:~# curl -sI 127.0.0.1:80
root@e514b399d69d:~#
HTTP/1.1 200 OK
Date: Fri, 24 Mar 2017 07:11:52 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Link: <http://127.0.0.1/?rest_route=/>; rel="https://api.w.org/"
Content-Type: text/html; charset=UTF-8

root@e514b399d69d:~# curl -s 127.0.0.1:80 | grep Holberton
<title>Holberton &#8211; Just another WordPress site</title>
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Feed" href="http://127.0.0.1/?feed=rss2" />
<link rel="alternate" type="application/rss+xml" title="Holberton &raquo; Comments Feed" href="http://127.0.0.1/?feed=comments-rss2" />
        <div id="wp-custom-header" class="wp-custom-header"><img src="http://127.0.0.1/wp-content/themes/twentyseventeen/assets/images/header.jpg" width="2000" height="1200" alt="Holberton" /></div>  </div>
                            <h1 class="site-title"><a href="http://127.0.0.1/" rel="home">Holberton</a></h1>
        <p>Yet another bug by a Holberton student</p>
root@e514b399d69d:~#

```
Error checking on server 1 window:
```sh

root@27c0016e7502:/# apt-get install -y ruby
Reading package lists... Done
Building dependency tree       
Reading state information... Done
ruby is already the newest version.
ruby set to manually installed.
The following package was automatically installed and is no longer required:
  unzip
Use 'apt-get autoremove' to remove it.
0 upgraded, 0 newly installed, 0 to remove and 7 not upgraded.
root@27c0016e7502:/# gem install puppet-lint -v 2.1.1
Fetching: puppet-lint-2.1.1.gem (100%)
Successfully installed puppet-lint-2.1.1
1 gem installed
Installing ri documentation for puppet-lint-2.1.1...
Installing RDoc documentation for puppet-lint-2.1.1...
root@27c0016e7502:/# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Wed, 14 Aug 2024 08:05:31 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@27c0016e7502:/# sudo apt-get install tmux
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following package was automatically installed and is no longer required:
  unzip
Use 'apt-get autoremove' to remove it.
The following extra packages will be installed:
  libevent-2.0-5
The following NEW packages will be installed:
  libevent-2.0-5 tmux
0 upgraded, 2 newly installed, 0 to remove and 7 not upgraded.
Need to get 374 kB of archives.
After this operation, 895 kB of additional disk space will be used.
Do you want to continue? [Y/n] y
Get:1 http://archive.ubuntu.com/ubuntu/ trusty-updates/main libevent-2.0-5 amd64 2.0.21-stable-1ubuntu1.14.04.2 [126 kB]
Get:2 http://archive.ubuntu.com/ubuntu/ trusty/main tmux amd64 1.8-5 [247 kB]
Fetched 374 kB in 0s (1832 kB/s)
Selecting previously unselected package libevent-2.0-5:amd64.
(Reading database ... 28782 files and directories currently installed.)
Preparing to unpack .../libevent-2.0-5_2.0.21-stable-1ubuntu1.14.04.2_amd64.deb ...
Unpacking libevent-2.0-5:amd64 (2.0.21-stable-1ubuntu1.14.04.2) ...
Selecting previously unselected package tmux.
Preparing to unpack .../archives/tmux_1.8-5_amd64.deb ...
Unpacking tmux (1.8-5) ...
Setting up libevent-2.0-5:amd64 (2.0.21-stable-1ubuntu1.14.04.2) ...
Setting up tmux (1.8-5) ...
Processing triggers for libc-bin (2.19-0ubuntu6.9) ...
root@27c0016e7502:/# tmux
[exited]
root@27c0016e7502:/# grep -ro "phpp" /var/www/html
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-includes/js/zxcvbn.min.js:phpp
/var/www/html/wp-settings.php:phpp
root@27c0016e7502:/# grep -o "phpp" /var/www/html/wp-settings.php             
phpp
root@27c0016e7502:/# grep -n "phpp" /var/www/html/wp-settings.php
137:require_once( ABSPATH . WPINC . '/class-wp-locale.phpp' );
root@27c0016e7502:/# vi 0-strace_is_your_friend.pp
root@27c0016e7502:/# puppet apply 0-strace_is_your_friend.pp 
Notice: Compiled catalog for 27c0016e7502.ec2.internal in environment production in 0.21 seconds
Notice: /Stage[main]/Main/Exec[fix_bad_extension]/returns: executed successfully
Notice: Finished catalog run in 0.70 seconds

```
Error checking on server 2 window:
```sh

root@27c0016e7502:/# sudo strace -p 613
Process 613 attached
accept4(3, 
^CProcess 613 detached
 <detached ...>
root@27c0016e7502:/# sudo strace -p 708
strace: attach: ptrace(PTRACE_ATTACH, ...): No such process
root@27c0016e7502:/# 
root@27c0016e7502:/# sudo strace -p 227
Process 227 attached
accept4(3,  ^CProcess 227 detached
 <detached ...>
root@27c0016e7502:/# curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Wed, 14 Aug 2024 08:14:58 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

root@27c0016e7502:/# curl -s 127.0.0.1:80 | grep Holberton
root@27c0016e7502:/# sudo strace -p 227
Process 227 attached
accept4(3, {sa_family=AF_INET, sin_port=htons(35646), sin_addr=inet_addr("127.0.0.1")}, [16], SOCK_CLOEXEC) = 11
getsockname(11, {sa_family=AF_INET, sin_port=htons(80), sin_addr=inet_addr("127.0.0.1")}, [16]) = 0
fcntl(11, F_GETFL)                      = 0x2 (flags O_RDWR)
fcntl(11, F_SETFL, O_RDWR|O_NONBLOCK)   = 0
read(11, "HEAD / HTTP/1.1\r\nUser-Agent: cur"..., 8000) = 74
stat("/var/www/html/", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
stat("/var/www/html/index.html", 0x7ffdcb08d9e0) = -1 ENOENT (No such file or directory)
lstat("/var", {st_mode=S_IFDIR|0755, st_size=41, ...}) = 0
lstat("/var/www", {st_mode=S_IFDIR|0755, st_size=18, ...}) = 0
lstat("/var/www/html", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
lstat("/var/www/html/index.html", 0x7ffdcb08d9e0) = -1 ENOENT (No such file or directory)
stat("/var/www/html/index.cgi", 0x7ffdcb08d9e0) = -1 ENOENT (No such file or directory)
lstat("/var", {st_mode=S_IFDIR|0755, st_size=41, ...}) = 0
lstat("/var/www", {st_mode=S_IFDIR|0755, st_size=18, ...}) = 0
lstat("/var/www/html", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
lstat("/var/www/html/index.cgi", 0x7ffdcb08d9e0) = -1 ENOENT (No such file or directory)
stat("/var/www/html/index.pl", 0x7ffdcb08d9e0) = -1 ENOENT (No such file or directory)
lstat("/var", {st_mode=S_IFDIR|0755, st_size=41, ...}) = 0
lstat("/var/www", {st_mode=S_IFDIR|0755, st_size=18, ...}) = 0
lstat("/var/www/html", {st_mode=S_IFDIR|0755, st_size=4096, ...}) = 0
lstat("/var/www/html/index.pl", 0x7ffdcb08d9e0) = -1 ENOENT (No such file or directory)
stat("/var/www/html/index.php", {st_mode=S_IFREG|0644, st_size=418, ...}) = 0
setitimer(ITIMER_PROF, {it_interval={0, 0}, it_value={60, 0}}, NULL) = 0
rt_sigaction(SIGPROF, {0x7f66effa0a50, [PROF], SA_RESTORER|SA_RESTART, 0x7f66f3282cb0}, {0x7f66effa0a50, [PROF], SA_RESTORER|SA_RESTART, 0x7f66f3282cb0}, 8) = 0
rt_sigprocmask(SIG_UNBLOCK, [PROF], NULL, 8) = 0
getcwd("/", 4095)                       = 2
chdir("/var/www/html")                  = 0
setitimer(ITIMER_PROF, {it_interval={0, 0}, it_value={30, 0}}, NULL) = 0
fcntl(8, F_SETLK, {type=F_RDLCK, whence=SEEK_SET, start=1, len=1}) = 0
stat("/var/www/html/index.php", {st_mode=S_IFREG|0644, st_size=418, ...}) = 0
stat("/var/www/html/wp-blog-header.php", {st_mode=S_IFREG|0644, st_size=364, ...}) = 0
stat("/var/www/html/wp-load.php", {st_mode=S_IFREG|0644, st_size=3301, ...}) = 0
access("/var/www/html/wp-config.php", F_OK) = 0
stat("/var/www/html/wp-config.php", {st_mode=S_IFREG|0644, st_size=3047, ...}) = 0
stat("/var/www/html/wp-settings.php", {st_mode=S_IFREG|0644, st_size=16251, ...}) = 0
stat("/var/www/html/wp-includes/load.php", {st_mode=S_IFREG|0644, st_size=31394, ...}) = 0
stat("/var/www/html/wp-includes/default-constants.php", {st_mode=S_IFREG|0644, st_size=9489, ...}) = 0
stat("/var/www/html/wp-includes/plugin.php", {st_mode=S_IFREG|0644, st_size=31282, ...}) = 0
stat("/var/www/html/wp-includes/class-wp-hook.php", {st_mode=S_IFREG|0644, st_size=14460, ...}) = 0
stat("/var/www/html/wp-includes/version.php", {st_mode=S_IFREG|0644, st_size=619, ...}) = 0
stat("/usr/share/zoneinfo/UTC", {st_mode=S_IFREG|0644, st_size=118, ...}) = 0
access("/var/www/html/.maintenance", F_OK) = -1 ENOENT (No such file or directory)
access("/var/www/html/wp-content/languages", F_OK) = -1 ENOENT (No such file or directory)
stat("/var/www/html/wp-includes/languages", 0x7ffdcb08ad50) = -1 ENOENT (No such file or directory)
stat("/var/www/html/wp-includes/compat.php", {st_mode=S_IFREG|0644, st_size=17195, ...}) = 0
stat("/var/www/html/wp-includes/random_compat/random.php", {st_mode=S_IFREG|0644, st_size=7694, ...}) = 0
stat("/var/www/html/wp-includes/random_compat/byte_safe_strings.php", {st_mode=S_IFREG|0644, st_size=5651, ...}) = 0
stat("/var/www/html/wp-includes/random_compat/cast_to_int.php", {st_mode=S_IFREG|0644, st_size=2461, ...}) = 0
stat("/var/www/html/wp-includes/random_compat/error_polyfill.php", {st_mode=S_IFREG|0644, st_size=1533, ...}) = 0
access("/dev/urandom", R_OK)            = 0
stat("/var/www/html/wp-includes/random_compat/random_bytes_dev_urandom.php", {st_mode=S_IFREG|0644, st_size=4543, ...}) = 0
stat("/var/www/html/wp-includes/random_compat/random_int.php", {st_mode=S_IFREG|0644, st_size=5697, ...}) = 0
stat("/var/www/html/wp-includes/class-wp-list-util.php", {st_mode=S_IFREG|0644, st_size=6487, ...}) = 0
stat("/var/www/html/wp-includes/functions.php", {st_mode=S_IFREG|0644, st_size=174663, ...}) = 0
stat("/var/www/html/wp-includes/option.php", {st_mode=S_IFREG|0644, st_size=63787, ...}) = 0
stat("/var/www/html/wp-includes/class-wp-matchesmapregex.php", {st_mode=S_IFREG|0644, st_size=1913, ...}) = 0
stat("/var/www/html/wp-includes/class-wp.php", {st_mode=S_IFREG|0644, st_size=24136, ...}) = 0
stat("/var/www/html/wp-includes/class-wp-error.php", {st_mode=S_IFREG|0644, st_size=4664, ...}) = 0
stat("/var/www/html/wp-includes/pomo/mo.php", {st_mode=S_IFREG|0644, st_size=8462, ...}) = 0
stat("/var/www/html/wp-includes/pomo/translations.php", {st_mode=S_IFREG|0644, st_size=8779, ...}) = 0
stat("/var/www/html/wp-includes/pomo/entry.php", {st_mode=S_IFREG|0644, st_size=2887, ...}) = 0
stat("/var/www/html/wp-includes/pomo/streams.php", {st_mode=S_IFREG|0644, st_size=5948, ...}) = 0
stat("/var/www/html/wp-includes/class-phpass.php", {st_mode=S_IFREG|0644, st_size=7317, ...}) = 0
stat("/var/www/html/wp-includes/wp-db.php", {st_mode=S_IFREG|0644, st_size=95513, ...}) = 0
access("/var/www/html/wp-content/db.php", F_OK) = -1 ENOENT (No such file or directory)
socket(PF_LOCAL, SOCK_STREAM, 0)        = 12
fcntl(12, F_SETFL, O_RDONLY)            = 0
fcntl(12, F_GETFL)                      = 0x2 (flags O_RDWR)
connect(12, {sa_family=AF_LOCAL, sun_path="/var/run/mysqld/mysqld.sock"}, 110) = 0
setsockopt(12, SOL_SOCKET, SO_RCVTIMEO, "\2003\341\1\0\0\0\0\0\0\0\0\0\0\0\0", 16) = 0
setsockopt(12, SOL_SOCKET, SO_SNDTIMEO, "\2003\341\1\0\0\0\0\0\0\0\0\0\0\0\0", 16) = 0
setsockopt(12, SOL_IP, IP_TOS, [8], 4)  = -1 EOPNOTSUPP (Operation not supported)
setsockopt(12, SOL_SOCKET, SO_KEEPALIVE, [1], 4) = 0
read(12, "[\0\0\0\n5.5.54-0ubuntu0.14.04.1\0)\0\0"..., 16384) = 95
write(12, "U\0\0\1\5\242\16\0\0\0\0@\10\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"..., 89) = 89
read(12, "\7\0\0\2\0\0\0\2\0\0\0", 16384) = 11
poll([{fd=12, events=POLLIN|POLLPRI}], 1, 0) = 0 (Timeout)
write(12, "\22\0\0\0\3SET NAMES utf8mb4", 22) = 22
read(12, "\7\0\0\1\0\0\0\2\0\0\0", 16384) = 11
poll([{fd=12, events=POLLIN|POLLPRI}], 1, 0) = 0 (Timeout)
write(12, "1\0\0\0\3SET NAMES 'utf8mb4' COLLATE"..., 53) = 53
read(12, "\7\0\0\1\0\0\0\2\0\0\0", 16384) = 11
poll([{fd=12, events=POLLIN|POLLPRI}], 1, 0) = 0 (Timeout)
write(12, "\32\0\0\0\3SELECT @@SESSION.sql_mode", 30) = 30
read(12, "\1\0\0\1\1(\0\0\2\3def\0\0\0\22@@SESSION.sql_m"..., 16384) = 72
poll([{fd=12, events=POLLIN|POLLPRI}], 1, 0) = 0 (Timeout)
write(12, "\n\0\0\0\2wordpress", 14)    = 14
read(12, "\7\0\0\1\0\0\0\2\0\0\0", 16384) = 11
access("/var/www/html/wp-content/object-cache.php", F_OK) = -1 ENOENT (No such file or directory)
stat("/var/www/html/wp-includes/cache.php", {st_mode=S_IFREG|0644, st_size=22058, ...}) = 0
stat("/var/www/html/wp-includes/default-filters.php", {st_mode=S_IFREG|0644, st_size=25220, ...}) = 0
stat("/var/www/html/wp-includes/l10n.php", {st_mode=S_IFREG|0644, st_size=43130, ...}) = 0
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffdcb086bf0) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffdcb086ac0) = -1 ENOENT (No such file or directory)
lstat("/var/www/html/wp-includes/class-wp-locale.phpp", 0x7ffdcb088cf0) = -1 ENOENT (No such file or directory)
open("/var/www/html/wp-includes/class-wp-locale.phpp", O_RDONLY) = -1 ENOENT (No such file or directory)
chdir("/")                              = 0
write(12, "\1\0\0\0\1", 5)              = 5
shutdown(12, SHUT_RDWR)                 = 0
close(12)                               = 0
setitimer(ITIMER_PROF, {it_interval={0, 0}, it_value={0, 0}}, NULL) = 0
fcntl(8, F_SETLK, {type=F_UNLCK, whence=SEEK_SET, start=0, len=0}) = 0
setitimer(ITIMER_PROF, {it_interval={0, 0}, it_value={0, 0}}, NULL) = 0
writev(11, [{"HTTP/1.0 500 Internal Server Err"..., 187}], 1) = 187
write(7, "127.0.0.1 - - [14/Aug/2024:08:16"..., 87) = 87
times({tms_utime=5, tms_stime=3, tms_cutime=0, tms_cstime=0}) = 8529470506
shutdown(11, SHUT_WR)                   = 0
poll([{fd=11, events=POLLIN}], 1, 2000) = 1 ([{fd=11, revents=POLLIN|POLLHUP}])
read(11, "", 512)                       = 0
close(11)                               = 0
read(4, 0x7ffdcb08de97, 1)              = -1 EAGAIN (Resource temporarily unavailable)
accept4(3, ^CProcess 227 detached
 <detached ...>

```

Check if file is valid:
```sh

stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/alx-system_engineering-devops/0x17-web_stack_debugging_3$ puppet-lint 0-strace_is_your_friend.pp

```

File: `0-strace_is_your_friend.pp`
