#!/usr/bin/python3
'''
    module that contains a class that avoids dynamically
    created attributes
'''


class LockedClass:
    __locked__ = ['first_name']

    def __init__(self):
        '''init method'''
        pass
