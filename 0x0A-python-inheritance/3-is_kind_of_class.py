#!/usr/bin/python3
'''
    module that returns bool if obj is an instance of a class
'''


def is_kind_of_class(obj, a_class):
    '''function that rets True/False if obj is an instance

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False if otherwise
    '''

    return isinstance(obj, a_class)
