#!/usr/bin/python3
"""
Function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords.
"""

import requests


def count_words(subreddit, word_list, after="", word_count=None, count=0):
    """Counts the occurrences of keywords in the
    titles of hot articles for a given subreddit.
    """
    if word_count is None:
        word_count = {}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        'limit': 100,
        'after': after,
        'count': count
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
        )
        if response.status_code != 200:
            return
        data = response.json().get("data", {})
        children = data.get("children", [])
        if not children:
            return
        for post in children:
            title = post.get("data", {}).get("title", "").lower()
            for word in word_list:
                word_lower = word.lower()
                word_count[word_lower] = (
                    word_count.get(word_lower, 0)
                    + title.split().count(word_lower)
                )
        after = data.get("after")
        count += data.get("dist", 0)
        if after is None:
            if len(word_count) == 0:
                print("")
                return
            sorted_word_count = sorted(
                word_count.items(),
                key=lambda kv: (-kv[1], kv[0])
            )
            for word, count in sorted_word_count:
                if count > 0:
                    print("{}: {}".format(word, count))
            return
        return count_words(subreddit, word_list, after, word_count, count)
    except requests.RequestException:
        return
