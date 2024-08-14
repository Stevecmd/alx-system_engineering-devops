#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed on a subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            print(None)
            return
        try:
            data = response.json().get("data", {}).get("children", [])
        except ValueError:
            print(None)
            return
        if not data:
            print(None)
            return
        for post in data:
            print(post.get("data", {}).get("title"))
    except requests.RequestException:
        print(None)
