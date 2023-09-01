#!/usr/bin/python3
'''Python script that shows the last 10 commits of a repo'''
from requests import get, auth
import sys


if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
        rq = get(url)
        json_o = rq.json()
        for idx in range(0, 10):
            print("{}: {}".format(json_o[idx].get('sha'), json_o[idx].get('commit')
                                  .get('author').get('name')))
    except Exception:
        pass
