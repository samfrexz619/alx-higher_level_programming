#!/usr/bin/python3
'''importing Rectangle file'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class to define a square from Rectangle class'''

    def __init__(self, size):
        '''method to init sqaure'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        '''method to ret a str with the area'''
        return super().area()

    def __str__(self):
        '''method that ret a printable str'''
        return f'[Square] {self.__size}/{self.__size}'
