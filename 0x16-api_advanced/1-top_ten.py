#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import json
import requests
import sys


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
        if response.status_code == 404:
            print(None)
            return
        response.raise_for_status()
    except requests.RequestException as e:
        print("Error:", e)
        return None

    try:
        data = response.json()
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)
        return

    if not data or "data" not in data or "children" not in data["data"]:
        print("No data found")
        return

    for post in data["data"]["children"]:
        print(post["data"]["title"])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-top_ten.py <subreddit>")
        sys.exit(1)
