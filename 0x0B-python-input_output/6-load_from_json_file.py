#!/usr/bin/python3
'''module to create json-str from an obj'''


def load_from_json_file(filename):
    '''importing json'''
    import json

    '''function to create json str

    Args:
        filename: file

    '''
    with open(filename) as f:
        new_obj = f.read()

    return json.loads(new_obj)
