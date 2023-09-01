#!/usr/bin/python3
'''Python script that sends a request to the URL'''
import requests
import sys


if __name__ == "__main__":
    try:
        rs = requests.get(sys.argv[1])
        print(rs.headers['X-Request-Id'])
    except Exception:
        pass
