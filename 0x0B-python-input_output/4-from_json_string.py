#!/usr/bin/python3
'''module to create json-str from an obj'''


def from_json_string(my_str):
    '''importing json'''
    import json

    '''function to create json str

    Arg:
        my_str: string

    '''

    return json.loads(my_str)
