#!/usr/bin/python3
'''
    module that rets boolif obj is an instance of a class
'''


def inherits_from(obj, a_class):
    '''function that rets True/False if an obj is an instance of a class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj is an instance of a_class
        False if otherwise
    '''

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
