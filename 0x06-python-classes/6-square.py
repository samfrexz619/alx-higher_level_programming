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
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        '''method that ret position val'''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''method taht sets the position'''
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''method that returns the square'''
        return (self.__size ** 2)

    def my_print(self):
        '''method that prints in stdout the square with the character'''
        if self.__size == 0:
            print()
        else:
            for idx in range(self.__position[1]):
                print()
            for i in range(0, self.__size):
                for ij in range(self.position[0]):
                    print(' ', end='')
                for k in range(self.size):
                    print('#', end='')
                print()
