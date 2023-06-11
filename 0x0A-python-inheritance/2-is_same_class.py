#!/usr/bin/python3
'''
    module that ret True if the obj is exactly an instance
'''


def is_same_class(obj, a_class):
    '''function to ret True/False if obj is a type of a_class

    Args:
        obj: object
        a_class: class type

    Returns:
        True if obj type is a_class
        False if otherwise

    '''

    return type(obj) is a_class
