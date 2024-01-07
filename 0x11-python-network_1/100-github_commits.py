#!/usr/bin/python3
"""Listing 10 commits in a repo"""

if __name__ == "__main__":

    import requests
    from sys import argv

    repo = argv[1]
    owner = argv[2]
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    try:
        r = requests.get(url)
        result = r.json()
        for i in range(0, 10):
            sha = result[i].get('sha')
            author = result[i].get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    except Exception:
        pass
