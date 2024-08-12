# 0x11. What happens when you type google.com in your browser and press Enter
## Background Context
Being a Full-Stack Software Engineer means you’re comfortable interacting with any layer of the stack. <br />

A way to easily assess this is to simply ask an engineer to explain how a software system works. They can have a general overview of the flow or can choose to dig deep in a certain area. <br />

Let’s practice by exploring the infrastructure side (network, servers, security…) of the question. <br />

## Tasks
0. What happens when... 
This question is a classic and still widely used interview question for many types of software engineering position. <br /> 
It is used to assess a candidate’s general knowledge of how the web stack works on top of the internet. <br />
One important guideline to begin answering this question is that you should ask your interviewer whether <br />
they would like you to focus in on one specific area of the workflow. <br />
For a front-end position they may want you to talk at length about how the DOM is rendering. <br />
For an SRE position they may want you to go into the load balancing mechanism.

<br />
This question is a good test of whether you understand DNS. <br />
Many software engineering candidates struggle with this concept, so if you do well on this question, <br />
you are already way ahead of the curve. <br />
If you take this project seriously and write an excellent article, it may be something that will grab the attention of future employers.
<br />

Write a blog post explaining what happens when you type `https://www.google.com` in your browser and press Enter.
<br />

Requirements, your post must cover:

- DNS request
- TCP/IP
- Firewall
- HTTPS/SSL
- Load-balancer
- Web server
- Application server
- Database
File: `0-blog_post`

1. Everything's better with a pretty diagram
Add a schema to your blog post illustrating the flow of the request created when you type `https://www.google.com` in your browser and press `Enter`.

The diagram should show:

- DNS resolution
- that the request hitting server IP on the appropriate port
- that the traffic is encrypted
- that the traffic goes through a firewall
- that the request is distributed via a load balancer
- that the web server answers the request by serving a web page
- that the application server generates the web page
- that the application server request data from the database

Example diagram:
![Example Schema](https://imgur.com/i9ivkdo)

File: `1-what_happen_when_diagram`

2. Contribute!
Folks on the Internet have been trying to put together a comprehensive answer to the question. Help them by submitting a pull request. Paste the link in your answer file.

`https://github.com/alex/what-happens-when#the-g-key-is-pressed`

Requirements:

- The pull request must bring meaningful value (not a typo correction or style improvement)
- Share the pull request URL in your answer file and in the field below

File: `2-contribution-to_what-happens-when_github_answer`
