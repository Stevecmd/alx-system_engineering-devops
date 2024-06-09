# 0x09. Web infrastructure design 
## Tasks
0. Simple web stack

A lot of websites are powered by simple web infrastructure, a lot of time it is composed of a single server with a `LAMP stack`.

On a whiteboard, design a one server web infrastructure that hosts the website that is reachable via `www.foobar.com`. Start your explanation by having a user wanting to access your website.

Requirements:

- You must use:
    - 1 server
    - 1 web server (Nginx)
    - 1 application server
    - 1 application files (your code base)
    - 1 database (MySQL)
    - 1 domain name `foobar.com` configured with a www record that points to your server IP `8.8.8.8`
- You must be able to explain some specifics about this infrastructure:
    - What is a server
    - What is the role of the domain name
    - What type of DNS record `www` is in `www.foobar.com`
    - What is the role of the web server
    - What is the role of the application server
    - What is the role of the database
    - What is the server using to communicate with the computer of the user requesting the website
- You must be able to explain what the issues are with this infrastructure:
    - SPOF
    - Downtime when maintenance needed (like deploying new code web server needs to be restarted)
    - Cannot scale if too much incoming traffic

Please, remember that everything must be written in English to further your technical ability in a variety of settings.

## Answers
### What is a Database?
A **database** is an organized collection of structured information or data, typically stored electronically in a computer system. A database is managed by a database management system (DBMS). Together, the data and the DBMS, along with the applications associated with them, are referred to as a database system. Databases are used to store, manage, and retrieve information efficiently.

### Difference Between a Web Server and an App Server
- **Web Server**: 
  - **Primary Function**: Serves static content like HTML, CSS, JavaScript, and images to the web browser.
  - **Common Examples**: Apache HTTP Server, Nginx.
  - **Protocol**: Primarily HTTP/HTTPS.
  - **Usage**: Handles requests from clients (browsers) and delivers web pages.

- **App Server**:
  - **Primary Function**: Serves dynamic content and executes business logic. It can also serve static content, but it is designed to create dynamic content on the fly.
  - **Common Examples**: Apache Tomcat, JBoss, WebSphere.
  - **Protocol**: Supports multiple protocols including HTTP, but also more complex protocols such as RMI/IIOP.
  - **Usage**: Manages application operations between users and back-end business applications or databases.

### What is DNS?
The Domain Name System is a bit like a postal service. <br>There are millions of DNS servers carrying DNS records information to users about the websites they are visiting. <br>Each server in the delivery chain needs to be up-to-date with the latest information within the DNS records.

Servers that contact your website regularly save relevant DNS records to help everything work smoothly. This process is a bit like jotting down favorite addresses for safe-keeping. <br>These handy records (also called ‘cache’ records) include, but are not limited to, your DNS hosting “address” or nameserver (NS) record.
### DNS Record Types
- **A (Address) Record**: Maps a domain to a specific IPv4 Address.
- **AAAA (IPv6 Address) Record**: Maps a domain to an IPv6 address.
- **CNAME (Canonical Name) Record**: Alias of one name to another. The DNS lookup will continue by retrying the lookup with the new name.
- **MX (Mail Exchange) Record**: Specifies the mail server responsible for receiving email on behalf of a domain.
- **TXT (Text) Record**: Holds text information for various purposes. Often used for SPF, DKIM, and DMARC policies.
- **NS (Name Server) Record**: Specifies the authoritative DNS servers for a domain.
- **SRV (Service) Record**: Specifies a port for specific services.
- **PTR (Pointer) Record**: Used for reverse DNS lookups.

![NameServers](https://namecheap.simplekb.com/SiteContents/2-7C22D5236A4543EB827F3BD8936E153E/media/dnsexplained3.png)

[Further Reading](https://www.namecheap.com/support/knowledgebase/article.aspx/10594/10/all-types-of-dns-records-explained/)

### Single Point of Failure
A **single point of failure (SPOF)** is a part of a system that, if it fails, will stop the entire system from working. SPOFs are undesirable in any system with a goal of high availability or reliability, such as a production environment or critical infrastructure.

### How to Avoid Downtime When Deploying New Code
- **Blue-Green Deployment**: Maintain two identical production environments (Blue and Green). Deploy new code to the Blue environment while Green serves the current production traffic, then switch.
- **Canary Release**: Gradually roll out the new code to a small subset of users before a full-scale deployment.
- **Rolling Update**: Gradually update instances of the application, ensuring some instances are always available.
- **Feature Toggles**: Deploy new code with features turned off, and enable them gradually or instantly once verified.
- **Automated Testing**: Extensive unit, integration, and end-to-end tests to catch issues before deployment.
- **Zero-Downtime Deployment Tools**: Use of CI/CD tools that support zero-downtime deployments, like Kubernetes, which allows rolling updates and rollbacks.

### High Availability Cluster (Active-Active / Active-Passive)
- **Active-Active Cluster**: All nodes are active and handle traffic simultaneously. If one node fails, the others continue to handle the load.
- **Active-Passive Cluster**: Only one node is active at a time. The passive node(s) remain on standby and take over if the active node fails.

### What is HTTPS
**HTTPS (HyperText Transfer Protocol Secure)** is the secure version of HTTP. It uses SSL/TLS to encrypt the data sent between the client and server, ensuring data integrity and privacy. HTTPS is essential for protecting sensitive data such as login credentials and payment information.

### What is a Firewall
A **firewall** is a network security device or software that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Firewalls establish a barrier between trusted internal networks and untrusted external networks, such as the internet. There are different types of firewalls, including packet-filtering firewalls, stateful inspection firewalls, proxy firewalls, and next-generation firewalls (NGFW).

File: `0-simple_web_stack`

1. Distributed web infrastructure

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`.

Requirements:

- You must add:
    - 2 servers
    - 1 web server (Nginx)
    - 1 application server
    - 1 load-balancer (HAproxy)
    - 1 set of application files (your code base)
    - 1 database (MySQL)
- You must be able to explain some specifics about this infrastructure:
    - For every additional element, why you are adding it
    - What distribution algorithm your load balancer is configured with and how it works
    - Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both
    - How a database Primary-Replica (Master-Slave) cluster works
    - What is the difference between the Primary node and the Replica node in regard to the application
- You must be able to explain what the issues are with this infrastructure:
    - Where are SPOF
    - Security issues (no firewall, no HTTPS)
    - No monitoring


File: `1-distributed_web_infrastructure`

2. Secured and monitored web infrastructure

On a whiteboard, design a three server web infrastructure that hosts the website `www.foobar.com`, it must be secured, serve encrypted traffic, and be monitored.

Requirements:

- You must add:
    - 3 firewalls
    - 1 SSL certificate to serve `www.foobar.com` over HTTPS
    - 3 monitoring clients (data collector for Sumologic or other monitoring services)
- You must be able to explain some specifics about this infrastructure:
    - For every additional element, why you are adding it
    - What are firewalls for
    - Why is the traffic served over HTTPS
    - What monitoring is used for
    - How the monitoring tool is collecting data
    - Explain what to do if you want to monitor your web server QPS
- You must be able to explain what the issues are with this infrastructure:
    - Why terminating SSL at the load balancer level is an issue
    - Why having only one MySQL server capable of accepting writes is an issue
    - Why having servers with all the same components (database, web server and application server) might be a problem

Please, remember that everything must be written in English to further your technical ability in a variety of settings.

File: `2-secured_and_monitored_web_infrastructure`

3. Scale up 

Requirements:

- You must add:
    - 1 server
    - 1 load-balancer (HAproxy) configured as cluster with the other one
    - Split components (web server, application server, database) with their own server
- You must be able to explain some specifics about this infrastructure:
    - For every additional element, why you are adding it

Please, remember that everything must be written in English to further your technical ability in a variety of settings.


File: `3-scale_up`