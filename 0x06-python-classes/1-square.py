#!/usr/bin/python3
'''defines a class of a Square'''


class Square:
    '''a class that defines the size of a square'''
    def __init__(self, size=0):
        '''method to init square

        Args:
            param (int): size of the square
        '''
        self.__size = size
