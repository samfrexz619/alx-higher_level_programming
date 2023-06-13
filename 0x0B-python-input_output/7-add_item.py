#!/usr/bin/python3
'''module to load and save data from a file'''


import sys
import os

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

ls = []
if os.path.exists('add_item.json'):
    ls = load_from_json_file('add_item.json')

for idx in sys.argv[1:]:
    ls.append(idx)

save_to_json_file(ls, 'add_item.json')
