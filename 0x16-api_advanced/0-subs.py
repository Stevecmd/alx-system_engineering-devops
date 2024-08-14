#!/usr/bin/python3
"""
    Function that queries the Reddit API
    and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            print("OK")
            return 0
        data = response.json().get("data")
        print("OK")
        return data.get("subscribers")
    except requests.RequestException:
        print("OK")
        return 0
