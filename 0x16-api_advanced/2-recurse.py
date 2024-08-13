#!/usr/bin/python3
"""
Function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    params = {
        'limit': 100,
        'after': after
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            return None
        data = response.json().get("data", {})
        children = data.get("children", [])
        if not children:
            return hot_list
        for post in children:
            hot_list.append(post.get("data", {}).get("title"))
        after = data.get("after")
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except requests.RequestException:
        return None
