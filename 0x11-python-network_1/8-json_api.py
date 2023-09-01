#!/usr/bin/python3
'''
Python script that sends a POST request to the URL
'''
import requests
import sys


if __name__ == "__main__":
    data = {'q': ""}

    try:
        data['q'] = sys.argv[1]
    except Exception:
        pass

    rs = requests.post('http://0.0.0.0:5000/search_user', data)

    try:
        json_o = rs.json()
        if not json_o:
            print("No result")
        else:
            print("[{}] {}".format(json_o.get('id'), json_o.get('name')))
    except Exception:
        print("Not a valid JSON")
