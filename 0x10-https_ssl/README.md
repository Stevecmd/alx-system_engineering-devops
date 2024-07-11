# 0x10. HTTPS SSL
### Requirements
#### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass `Shellcheck` (version `0.3.7`) without any error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

### Activate a Virtual environment
1. Create a Virtual Environment:
```sh
python3 -m venv venv
```
2. Activate the Virtual Environment:
```sh
source venv/bin/activate
```
3. Deactivate the Virtual Environment:
```sh
deactivate
```

### Tasks
0. World wide web
Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

- Add the subdomain `www` to your domain, point it to your `lb-01` IP (your domain name might be configured with default subdomains, feel free to remove them)
- Add the subdomain `lb-01` to your domain, point it to your `lb-01` IP
- Add the subdomain `web-01` to your domain, point it to your `web-01` IP
- Add the subdomain `web-02` to your domain, point it to your `web-02` IP
- Your Bash script must accept 2 arguments:
        1. `domain`:
            - type: string
            - what: domain name to audit
            - mandatory: yes
        2. `subdomain`:
            - type: string
            - what: specific subdomain to audit
            - mandatory: no
- Output: `The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]`
- When only the parameter `domain` is provided, display information for its subdomains `www`, `lb-01`, `web-01` and `web-02` - in this specific order
- When passing `domain` and subdomain parameters, display information for the specified subdomain
- Ignore `shellcheck` case `SC2086`
- Must use:
    - `awk`
    - at least one Bash function
- You do not need to handle edge cases such as:
    - Empty parameters
    - Nonexistent domain names
    - Nonexistent subdomains
Example:
```sh

sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
www.holberton.online.   87  IN  A   54.210.47.110
sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
lb-01.holberton.online. 101 IN  A   54.210.47.110
sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-01.holberton.online. 212    IN  A   34.198.248.145
sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
;; ANSWER SECTION:
web-02.holberton.online. 298    IN  A   54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online
The subdomain www is a A record and points to 54.210.47.110
The subdomain lb-01 is a A record and points to 54.210.47.110
The subdomain web-01 is a A record and points to 34.198.248.145
The subdomain web-02 is a A record and points to 54.89.38.100
sylvain@ubuntu$
sylvain@ubuntu$ ./0-world_wide_web holberton.online web-02
The subdomain web-02 is a A record and points to 54.89.38.100

```
To run script, install dig utility
```sh

sudo apt-get update
sudo apt-get install dnsutils
dig -v

```

Confirming if my servers and load balancer are online:
```sh

stevecmd@DESKTOP-UTB295U:~/ALX/alx-system_engineering-devops/0x10-https_ssl$ curl -sI lb-01.stevecloud.tech
HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Thu, 11 Jul 2024 08:49:27 GMT
content-type: text/html
content-length: 612
last-modified: Wed, 10 Jul 2024 04:32:07 GMT
etag: "668e0ec7-264"
accept-ranges: bytes

stevecmd@DESKTOP-UTB295U:~/ALX/alx-system_engineering-devops/0x10-https_ssl$ curl -sI web-01.stevecloud.tech
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 11 Jul 2024 08:49:41 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Tue, 21 Apr 2020 14:09:01 GMT
Connection: keep-alive
ETag: "5e9efe7d-264"
Accept-Ranges: bytes

stevecmd@DESKTOP-UTB295U:~/ALX/alx-system_engineering-devops/0x10-https_ssl$ curl -sI web-02.stevecloud.tech
HTTP/1.1 200 OK
Server: nginx/1.18.0 (Ubuntu)
Date: Thu, 11 Jul 2024 08:49:52 GMT
Content-Type: text/html
Content-Length: 612
Last-Modified: Wed, 10 Jul 2024 04:32:07 GMT
Connection: keep-alive
ETag: "668e0ec7-264"
Accept-Ranges: bytes

```
File: `0-world_wide_web`

Log into the load balancer:
```sh
(venv) stevecmd@DESKTOP-UTB295U:~/ALX/alx-system_engineering-devops/0x10-https_ssl$ ssh ubuntu@lb-01.stevecloud.tech -y

```


input details below ie domain, then run it each command:
```sh

sudo apt update -y
sudo apt install snapd -y
sudo apt-get remove certbot
sudo apt-get install certbot -y
sudo service haproxy stop
sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d www.example.com
sudo ls /etc/letsencrypt/live/www.stevecloud.tech
sudo mkdir -p /etc/haproxy/certs
DOMAIN='www.stevecloud.tech' sudo -E bash -c 'cat /etc/letsencrypt/live/$DOMAIN/fullchain.pem /etc/letsencrypt/live/$DOMAIN/privkey.pem > /etc/haproxy/certs/$DOMAIN.pem'
sudo chmod -R go-rwx /etc/haproxy/certs
sudo nano /etc/haproxy/haproxy.cfg

```
Installing Certbot and setting up server:
```sh

ubuntu@197045-lb-01:~$ sudo certbot certonly --standalone --preferred-challenges http --http-01-port 80 -d www.stevecloud.tech
Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator standalone, Installer None
Enter email address (used for urgent renewal and security notices) (Enter 'c' to
cancel): murimi101@gmail.com

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Please read the Terms of Service at
https://letsencrypt.org/documents/LE-SA-v1.4-April-3-2024.pdf. You must agree in
order to register with the ACME server at
https://acme-v02.api.letsencrypt.org/directory
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(A)gree/(C)ancel: A

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Would you be willing to share your email address with the Electronic Frontier
Foundation, a founding partner of the Let's Encrypt project and the non-profit
organization that develops Certbot? We'd like to send you email about our work
encrypting the web, EFF news, campaigns, and ways to support digital freedom.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
(Y)es/(N)o: Y
Obtaining a new certificate
Performing the following challenges:
http-01 challenge for www.stevecloud.tech
Cleaning up challenges

IMPORTANT NOTES:
 - Your account credentials have been saved in your Certbot
   configuration directory at /etc/letsencrypt. You should make a
   secure backup of this folder now. This configuration directory will
   also contain certificates and private keys obtained by Certbot so
   making regular backups of this folder is ideal.
 - We were unable to subscribe you the EFF mailing list because your
   e-mail address appears to be invalid. You can try again later by
   visiting https://act.eff.org.

```
Confirmation:
```sh

ubuntu@197045-lb-01:~$ sudo lsof -i :80
COMMAND   PID    USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
haproxy 18154 haproxy    7u  IPv4  89236      0t0  TCP *:http (LISTEN)
ubuntu@197045-lb-01:~$ dig www.stevecloud.tech

; <<>> DiG 9.16.48-Ubuntu <<>> www.stevecloud.tech
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 5784
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;www.stevecloud.tech.           IN      A

;; ANSWER SECTION:
www.stevecloud.tech.    300     IN      A       3.84.158.236

;; Query time: 264 msec
;; SERVER: 127.0.0.53#53(127.0.0.53)
;; WHEN: Thu Jul 11 09:46:33 UTC 2024
;; MSG SIZE  rcvd: 64

```
See the certificates:
```sh

ubuntu@197045-lb-01:~$ sudo ls /etc/letsencrypt/live/www.stevecloud.tech
README  cert.pem  chain.pem  fullchain.pem  privkey.pem

```

1. HAproxy SSL termination
“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www..`

Requirements:

- HAproxy must be listening on port TCP 443
- HAproxy must be accepting SSL traffic
- HAproxy must serve encrypted traffic that will return the `/` of your web server
- When querying the root of your domain name, the page returned must contain `Holberton School`
- Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)

The file `1-haproxy_ssl_termination` must be your HAproxy configuration file

Make sure to install HAproxy 1.5 or higher, `SSL termination` is not available before v1.5.

Example:
```sh
sylvain@ubuntu$ curl -sI https://www.holberton.online
HTTP/1.1 200 OK
Server: nginx/1.4.6 (Ubuntu)
Date: Tue, 28 Feb 2017 01:52:04 GMT
Content-Type: text/html
Content-Length: 30
Last-Modified: Tue, 21 Feb 2017 07:21:32 GMT
ETag: "58abea7c-1e"
X-Served-By: 03-web-01
Accept-Ranges: bytes
sylvain@ubuntu$
sylvain@ubuntu$ curl https://www.holberton.online
Holberton School for the win!
sylvain@ubuntu$
```
File: `1-haproxy_ssl_termination`

2. No loophole in your website traffic
A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

Requirements:

- This should be transparent to the user
- HAproxy should return a `301`
- HAproxy should redirect HTTP traffic to HTTPS
- Share your HAproxy config as an answer file (`/etc/haproxy/haproxy.cfg`)
NB: Shutdown HAProxy before running the script below.
The file `100-redirect_http_to_https` must be your HAproxy configuration file
```sh

(venv) stevecmd@DESKTOP-UTB295U:~/ALX/AirBnB_clone_v2$ curl -sIL http://www.stevecloud.tech
HTTP/1.1 301 Moved Permanently
content-length: 0
location: https://www.stevecloud.tech/

HTTP/1.1 200 OK
server: nginx/1.18.0 (Ubuntu)
date: Thu, 11 Jul 2024 10:33:43 GMT
content-type: text/html
content-length: 612
last-modified: Tue, 21 Apr 2020 14:09:01 GMT
etag: "5e9efe7d-264"
accept-ranges: bytes

```
File: `100-redirect_http_to_https`