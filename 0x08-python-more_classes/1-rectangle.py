#!/usr/bin/python3
'''
    this module is a class that defines a Rectangle
'''

class Rectangle:
    '''this class defines a rectangle'''

    def __init__(self, width=0, height=0):
        '''method to init the instance

        Args:
            width: rectangle width
            height: rectangle height

        '''

        self.width = width
        self.height = height

    @property
    def width(self):
        '''method that rets width val

        Returns:
            rectangle width

        '''

        return self.__width

    @width.setter
    def width(self, value):
        '''method that defines width

        Arg:
            value: width

        Raises:
            TypeError: width not an int
            ValueError: width less than zero

        '''

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        '''method that rets height val

        Returns:
            height of the rectangle

        '''

        return self.__height

    @height.setter
    def height(self, value):
        '''method that defines height

        Args:
            value: width

        Raises:
            TypeError: if height not an int
            ValueError: if height less than zero

        '''

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value


