#!/usr/bin/python3
'''module to create json-str from an obj'''


def save_to_json_file(my_obj, filename):
    '''importing json'''
    import json

    '''function to create json str

    Args:
        my_obj: object
        filename: file

    '''
    with open(filename, 'w', encoding='utf-8') as f:
        new_file = json.dumps(my_obj)
        f.write(new_file)
