#!/usr/bin/python3
'''module that contains rectangle class'''


from models.base import Base


class Rectangle(Base):
    '''class Rectangle'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init instances'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width getter'''
        return self.__width


    @width.setter
    def width(self, val):
        '''width setter'''
        if type(val) is not int:
            raise TypeError('width must be an integer')
        if val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        '''height setter'''
        return self.__height

    @height.setter
    def height(self, val):
        '''height setter'''
        if type(val) is not int:
            raise TypeError('height must be an integer')
        if val <= 0:
            raise ValueError('height must be > 0')
        self.__height = value
