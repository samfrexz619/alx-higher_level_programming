#!/usr/bin/python3
'''module for myInt'''


class MyInt(int):
    '''Class that inherits from class int'''

    def __eq__(self, other):
        '''Method to rets != check'''
        return int.__ne__(self, other)

    def __ne__(self, other):
        '''Method that ret == check'''
        return int.__eq__(self, other)
