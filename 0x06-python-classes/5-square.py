#!/usr/bin/python3
'''Define a class Square'''


class Square:
    '''class that defines a square size'''
    def __init__(self, size=0):
        '''method to init square obj'''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def area(self):
        '''method that returns the sq of the obj'''
        return (self.__size ** 2)

    @property
    def size(self):
        '''method that returns the size val'''
        return (self.__size)

    @size.setter
    def size(self, value):
        '''method to set the size value'''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def my_print(self):
        '''method that prints in stdout the square with the character'''
        if not self.__size:
            print()
        else:
            for idx in range(self.__size):
                for ij in range(self.__size):
                    print('#', end='')
                print()
