#!/usr/bin/python3
'''defines a class of a Square'''


class Square:
    '''a class that defines the size of a square'''
    def __init__(self, size=0):
        '''method to init square'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = int(size)
