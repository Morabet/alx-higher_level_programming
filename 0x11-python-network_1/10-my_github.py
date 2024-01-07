#!/usr/bin/python3
"""Take GitHub credentials (username and password) as arguments
and uses the GitHub API to display users id"""

if __name__ == "__main__":

    import requests
    from sys import argv

    url = 'https://api.github.com/user'
    username = argv[1]
    token = argv[2]
    try:
        r = requests.get(url, auth=(username, token))
        result = r.json()
        print(f"{result.get('id')}")
    except Exception:
        pass
