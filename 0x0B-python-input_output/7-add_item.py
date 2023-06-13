#!/usr/bin/python3
'''module to load and save data from a file'''


import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if os.path.exists('add_item.json') is True:
    ls = list(load_from_json_file('add_item.json'))
    for idx in range(1, len(sys.argv)):
        ls.append(sys.argv[idx])

    save_to_json_file(ls, 'add_item.json')
else:
    ls = []
    save_to_json_file(ls, 'add_item.json')
