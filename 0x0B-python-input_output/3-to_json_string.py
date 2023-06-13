#!/usr/bin/python3
'''module to create json-str from an obj'''


def to_json_string(my_obj):
    '''importing json'''
    import json

    '''function to create json str

    Arg:
        my_obj: object

    '''

    return json.dumps(my_obj)
