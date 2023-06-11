#!/usr/bin/python3
def lookup(obj):
    '''function that returns the list of available attr

    Args:
        obj: instance of class

    Returns:
        list of attrs
    '''

    return dir(obj)
