#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request and displays the value
'''
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        html = res.info()
        print(html.get('X-Request-Id'))
