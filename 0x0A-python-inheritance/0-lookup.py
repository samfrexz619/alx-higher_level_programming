#!/usr/bin/python3
'''
    this module is a function that returns list
'''


def lookup(obj):
    '''function that returns the list of available attr

    Args:
        obj: instance of class

    Returns:
        list of attrs
    '''

    return dir(obj)
