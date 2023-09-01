#!/usr/bin/python3
'''
Python script that takes in a URL, sends a request and displays
the value
'''
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except error.HTTPError as err:
        print('Error code: {}'.format(err.code))
