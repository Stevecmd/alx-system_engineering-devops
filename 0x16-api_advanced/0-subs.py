#!/usr/bin/python3
"""
Function that queries the Reddit API
and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return 0
        data = response.json().get("data")
        return data.get("subscribers", 0)
    except requests.RequestException:
        return 0
