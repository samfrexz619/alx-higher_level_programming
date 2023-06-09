#!/usr/bin/python3
'''
    this module is a class that defines a Rectangle
'''


class Rectangle:
    '''this class defines a rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''method to init the instance

        Args:
            width: rectangle width
            height: rectangle height

        '''

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        '''method to calc the area of rectangle

        Returns:
            rectangle area

        '''

        return self.width * self.height

    def perimeter(self):
        '''method to calc rectangle perimeter

        Returns:
            reactangle perimeter

        '''

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * self.width) + (2 * self.height)

    def __str__(self):
        '''method to ret rect

        Returns:
            str of rect

        '''

        rect = ''

        if self.width == 0 or self.height == 0:
            return rect

        for idx in range(self.height):
            rect += ('#' * self.width) + '\n'

        return rect[:-1]

    def __repr__(self):
        '''method to return str rep of the instance

        Returns:
            str representation of the obj

        '''

        return f'Rectangle({self.width:d}, {self.height:d})'

    def __del__(self):
        '''method to print a msg when instance is del'''

        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
