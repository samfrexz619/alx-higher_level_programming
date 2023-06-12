#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    '''class to define a rectangle from base-geometric class'''

    def __init__(self, width, height):
        '''method to init instances'''
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
