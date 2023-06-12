#!/usr/bin/python3
'''module for attr of geometric class'''


class BaseGeometry:
    '''class to define the area of geometric shapes'''
    def area(self):
        '''method that defs the area of geometric shapes'''

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''method to receive value ppty

        Args:
            name: object name
            value: value of property

        '''

        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
