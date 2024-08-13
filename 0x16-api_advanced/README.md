# 0x16. API Advanced

## Resources

Read or watch:

- [Reddit API Documentation](https://www.reddit.com/dev/api/)
- [Query String](https://en.wikipedia.org/wiki/Query_string)

### General

- How to read API documentation to find the endpoints you’re looking for
- How to use an API with pagination
- How to parse JSON results from an API
- How to make a recursive API call
- How to sort a dictionary by value

## Background Context
Reddit is a popular social media platform where users can join communities (subreddits) based on their interests. <br /> 
Each subreddit has its own set of posts, discussions, and subscriber count. <br />
The Reddit API provides a way for developers to programmatically access and interact with the data available on Reddit. <br />
This project aims to leverage the Reddit API to extract useful information from subreddits and present it in a structured manner. <br />

The project is structured around several key tasks:

How many subs?: Write a function that queries the Reddit API and returns the number of subscribers for a given subreddit. If the subreddit is invalid, the function should return 0. <br />

Top Ten: Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. If the subreddit is invalid, the function should print None. <br />

Recurse it!: Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found, the function should return None. <br />

The project requires adherence to specific coding standards and practices, including the use of the PEP 8 style guide, organizing imports alphabetically, and ensuring all files are executable. Additionally, the project mandates the use of the Requests module for sending HTTP requests to the Reddit API and handling potential issues such as rate limiting by setting a custom User-Agent. <br />

By completing this project, developers will gain experience in working with APIs, handling JSON data, implementing recursive functions, and following best practices in Python programming. <br />

## Project Description
This project involves creating Python scripts that interact with the Reddit API to retrieve and process data from various subreddits. The primary goal is to develop functions that can query the Reddit API to obtain information such as the number of subscribers, the titles of the top posts, and a list of all hot articles for a given subreddit. The project emphasizes the use of proper API documentation, handling pagination, parsing JSON responses, and implementing recursive API calls.

## Requirements
### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- Libraries imported in your Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- You must use the Requests module for sending HTTP requests to the Reddit API

## Tasks
0. How many subs?
Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.

Requirements:

- Prototype: `def number_of_subscribers(subreddit)`
- If not a valid subreddit, return 0.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```sh

stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/alx-system_engineering-devops/0x16-api_advanced$ pycodestyle *.py
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/alx-system_engineering-devops/0x16-api_advanced$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/alx-system_engineering-devops/0x16-api_advanced$ python3 0-main.py programming
6354618
stevecmd@stevecmd-HP-ENVY-15-Notebook-PC:/media/stevecmd/48444E06444DF6EA/ALX/alx-system_engineering-devops/0x16-api_advanced$ python3 0-main.py this_is_a_fake_subreddit
0

```
File: `0-subs.py`


1. Top Ten
Write a function that queries the [Reddit API](https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:

- Prototype: `def top_ten(subreddit)`
- If not a valid subreddit, print None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

```sh

stevecmd@stevecmd-HP-Notebook-PC ~/reddit_api/project $ cat 1-main.py
#!/usr/bin/python3
"""
1-main
"""
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
stevecmd@stevecmd-HP-Notebook-PC ~/reddit_api/project $ python3 1-main.py programming
Firebase founder's response to last week's "Firebase Costs increased by 7000%!"
How a 64k intro is made
HTTPS on Stack Overflow: The End of a Long Road
Spend effort on your Git commits
It's a few years old, but I just discovered this incredibly impressive video of researchers reconstructing sounds from video information alone
From the D Blog: Introspection, Introspection Everywhere
Do MVC like it’s 1979
GitHub is moving to GraphQL for v4 of their API (v3 was a REST API)
Google Bug Bounty - The 5k Error Page
PyCon 2017 Talk Videos
stevecmd@stevecmd-HP-Notebook-PC ~/reddit_api/project $ python3 1-main.py this_is_a_fake_subreddit
None


```
File: `1-top_ten.py`



2. Recurse it!
Write a recursive function that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

Hint: The Reddit API uses pagination for separating pages of responses.

Requirements:

- Prototype: `def recurse(subreddit, hot_list=[])`
- Note: You may change the prototype, but it must be able to be called with just a subreddit supplied. AKA you can add a- counter, but it must work without supplying a starting value in the main.
- If not a valid subreddit, return None.
- NOTE: Invalid subreddits may return a redirect to search results. Ensure that you are not following redirects.

Your code will NOT pass if you are using a loop and not recursively calling the function! This /can/ be done with a loop but the point is to use a recursive function. :)
```sh

stevecmd@stevecmd-HP-Notebook-PC ~/reddit_api/project $ cat 2-main.py
#!/usr/bin/python3
"""
2-main
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
stevecmd@stevecmd-HP-Notebook-PC ~/reddit_api/project $ python3 2-main.py programming
932
stevecmd@stevecmd-HP-Notebook-PC ~/reddit_api/project $ python3 2-main.py this_is_a_fake_subreddit


```
File: `2-recurse.py`

## Usage

To use the scripts in this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Ensure you have Python 3 installed:
    ```bash
    python3 --version
    ```
## Acknowledgments
This project was completed as part of the ALX Software Engineering program.

