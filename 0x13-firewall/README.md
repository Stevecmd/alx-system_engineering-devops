# 0x13. Firewall
## More Info
As explained in the `web stack debugging` guide concept page, `telnet` is a very good tool to check if sockets are open with `telnet IP PORT`. For example, if you want to check if port 22 is open on `web-02`:
```sh

sylvain@ubuntu$ telnet web-02.holberton.online 22
Trying 54.89.38.100...
Connected to web-02.holberton.online.
Escape character is '^]'.
SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

Protocol mismatch.
Connection closed by foreign host.

```

We can see for this example that the connection is successful: `Connected to web-02.holberton.online.` <br />

Now let’s try connecting to port 2222:
```sh

sylvain@ubuntu$ telnet web-02.holberton.online 2222
Trying 54.89.38.100...
^C

```
We can see that the connection never succeeds, so after some time I just use `ctrl+c` to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your `web-02` server. If you SSH into your `web-02` server, the traffic will be originating from `web-02` and not from the school’s network, bypassing the firewall.

## Warning!

Containers on demand cannot be used for this project (Docker container limitation)

Be very careful with firewall rules! For instance, if you ever deny port `22/TCP` and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.

## Tasks
0. Block all incoming traffic but
Let’s install the `ufw` firewall and setup a few rules on `web-01`.

Requirements:

- The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won’t be checked)
- Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
    - `22` (SSH)
    - `443` (HTTPS SSL)
    - `80` (HTTP)
- Share the `ufw` commands that you used in your answer file
File: `0-block_all_incoming_traffic_but`

1. Port forwarding
Firewalls can not only filter requests, they can also forward them.

Requirements:

- Configure `web-01` so that its firewall redirects port `8080/TCP` to port `80/TCP`.
- Your answer file should be a copy of the `ufw` configuration file that you modified to make this happen

Terminal in `web-01`-
```sh

ubuntu@197045-web-01:~$ ufw status
ERROR: You need to be root to run this script
ubuntu@197045-web-01:~$ sudo ufw status
Status: inactive
ubuntu@197045-web-01:~$ sudo ufw default deny incoming
Default incoming policy changed to 'deny'
(be sure to update your rules accordingly)
ubuntu@197045-web-01:~$ sudo ufw default allow outgoing
Default outgoing policy changed to 'allow'
(be sure to update your rules accordingly)
ubuntu@197045-web-01:~$ sudo ufw allow 22/tcp
Rules updated
Rules updated (v6)
ubuntu@197045-web-01:~$ sudo ufw allow 80/tcp
Rules updated
Rules updated (v6)
ubuntu@197045-web-01:~$ sudo ufw allow 443/tcp
Rules updated
Rules updated (v6)
ubuntu@197045-web-01:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup
ubuntu@197045-web-01:~$ netstat -lpn

Command 'netstat' not found, but can be installed with:

sudo apt install net-tools

ubuntu@197045-web-01:~$ sudo apt install net-tools
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  net-tools
0 upgraded, 1 newly installed, 0 to remove and 75 not upgraded.
Need to get 196 kB of archives.
After this operation, 864 kB of additional disk space will be used.
Get:1 http://us-east-1.ec2.archive.ubuntu.com/ubuntu focal/main amd64 net-tools amd64 1.60+git20180626.aebd88e-1ubuntu1 [196 kB]
Fetched 196 kB in 0s (8855 kB/s)
Selecting previously unselected package net-tools.
(Reading database ... 123388 files and directories currently installed.)
Preparing to unpack .../net-tools_1.60+git20180626.aebd88e-1ubuntu1_amd64.deb ...
Unpacking net-tools (1.60+git20180626.aebd88e-1ubuntu1) ...
Setting up net-tools (1.60+git20180626.aebd88e-1ubuntu1) ...
Processing triggers for man-db (2.9.1-1) ...
ubuntu@197045-web-01:~$ netstat -lpn
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name    
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                   
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                   
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::22                   :::*                    LISTEN      -                   
udp        0      0 127.0.0.53:53           0.0.0.0:*                           -                   
udp        0      0 10.247.152.26:68        0.0.0.0:*                           -                   
raw6       0      0 :::58                   :::*                    7           -                   
Active UNIX domain sockets (only servers)
Proto RefCnt Flags       Type       State         I-Node   PID/Program name     Path
unix  2      [ ACC ]     STREAM     LISTENING     960295   68367/systemd        /run/user/1000/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     960301   68367/systemd        /run/user/1000/bus
unix  2      [ ACC ]     STREAM     LISTENING     960302   68367/systemd        /run/user/1000/gnupg/S.dirmngr
unix  2      [ ACC ]     STREAM     LISTENING     14438    -                    @/org/kernel/linux/storage/multipathd
unix  2      [ ACC ]     STREAM     LISTENING     960303   68367/systemd        /run/user/1000/gnupg/S.gpg-agent.browser
unix  2      [ ACC ]     STREAM     LISTENING     960304   68367/systemd        /run/user/1000/gnupg/S.gpg-agent.extra
unix  2      [ ACC ]     STREAM     LISTENING     960305   68367/systemd        /run/user/1000/gnupg/S.gpg-agent.ssh
unix  2      [ ACC ]     STREAM     LISTENING     960306   68367/systemd        /run/user/1000/gnupg/S.gpg-agent
unix  2      [ ACC ]     STREAM     LISTENING     960307   68367/systemd        /run/user/1000/pk-debconf-socket
unix  2      [ ACC ]     STREAM     LISTENING     960308   68367/systemd        /run/user/1000/snapd-session-agent.socket
unix  2      [ ACC ]     STREAM     LISTENING     20362    -                    /var/snap/lxd/common/lxd/unix.socket
unix  2      [ ACC ]     STREAM     LISTENING     20330    -                    /run/acpid.socket
unix  2      [ ACC ]     STREAM     LISTENING     14425    -                    /run/systemd/private
unix  2      [ ACC ]     STREAM     LISTENING     20344    -                    /run/dbus/system_bus_socket
unix  2      [ ACC ]     STREAM     LISTENING     14427    -                    /run/systemd/userdb/io.systemd.DynamicUser
unix  2      [ ACC ]     STREAM     LISTENING     20364    -                    /run/snapd.socket
unix  2      [ ACC ]     STREAM     LISTENING     20366    -                    /run/snapd-snap.socket
unix  2      [ ACC ]     STREAM     LISTENING     20369    -                    /run/uuidd/request
unix  2      [ ACC ]     STREAM     LISTENING     14436    -                    /run/lvm/lvmpolld.socket
unix  2      [ ACC ]     STREAM     LISTENING     14441    -                    /run/systemd/fsck.progress
unix  2      [ ACC ]     STREAM     LISTENING     14451    -                    /run/systemd/journal/stdout
unix  2      [ ACC ]     SEQPACKET  LISTENING     14456    -                    /run/udev/control
unix  2      [ ACC ]     STREAM     LISTENING     15160    -                    /run/systemd/journal/io.systemd.journal
unix  2      [ ACC ]     STREAM     LISTENING     25949    -                    /var/lib/amazon/ssm/ipc/health
unix  2      [ ACC ]     STREAM     LISTENING     20361    -                    @ISCSIADM_ABSTRACT_NAMESPACE
unix  2      [ ACC ]     STREAM     LISTENING     25952    -                    /var/lib/amazon/ssm/ipc/termination

ubuntu@197045-web-01:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
Nginx HTTP                 ALLOW       Anywhere                  
22/tcp                     ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
443/tcp                    ALLOW       Anywhere                  
Nginx HTTP (v6)            ALLOW       Anywhere (v6)             
22/tcp (v6)                ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
443/tcp (v6)               ALLOW       Anywhere (v6)  

```

- My web server `nginx` is only listening on port `80`
- `netstat` shows that nothing is listening on `8080`

Terminal in `web-02`:
```sh

ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:80
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:41 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
Accept-Ranges: bytes

ubuntu@03-web-02:~$ curl -sI web-01.holberton.online:8080
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 07 Mar 2017 02:14:43 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 04 Mar 2014 11:46:45 GMT
Connection: keep-alive
ETag: "5315bd25-264"
Accept-Ranges: bytes

ubuntu@03-web-02:~$

```
I use curl to query `web-01.holberton.online`, and since my firewall is forwarding the ports, I get a `HTTP 200` response on port `80/TCP` and also on port `8080/TCP`.

My work:
```sh

ubuntu@197045-web-01:~$ sudo ufw status
Status: active

To                         Action      From
--                         ------      ----
Nginx HTTP                 ALLOW       Anywhere                  
22/tcp                     ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
443/tcp                    ALLOW       Anywhere                  
Nginx HTTP (v6)            ALLOW       Anywhere (v6)             
22/tcp (v6)                ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
443/tcp (v6)               ALLOW       Anywhere (v6)             

ubuntu@197045-web-01:~$ ls
0-custom_http_response_header  0-nginx_likes_port_80  0-setup_web_static.sh  1  101-setup_web_static.pp  setup-nginx
ubuntu@197045-web-01:~$ vi 100-port_forwarding
ubuntu@197045-web-01:~$ sudo vi /etc/ufw/before.rules
ubuntu@197045-web-01:~$ sudo ufw allow 8080
Rule added
Rule added (v6)
ubuntu@197045-web-01:~$ sudo service ufw restart
ubuntu@197045-web-01:~$ sudo ufw enable
Command may disrupt existing ssh connections. Proceed with operation (y|n)? y
Firewall is active and enabled on system startup

```
When I opened "sudo vi /etc/ufw/before.rules" I added the rules below:
```sh

# Add the port forwarding rule
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT

```
File: `100-port_forwarding`
