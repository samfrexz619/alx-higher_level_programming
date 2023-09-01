#!/usr/bin/python3
'''
Python script that sends a request to the URL
'''
import requests
import sys


if __name__ == "__main__":
    rs = requests.get(sys.argv[1])
    if rs.status_code >= 400:
        print("Error code: {}".format(rs.status_code))
    else:
        print(rs.text)
