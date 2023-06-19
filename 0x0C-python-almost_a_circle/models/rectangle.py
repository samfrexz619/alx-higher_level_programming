#!/usr/bin/python3
'''module that contains rectangle class'''


from models.base import Base

'''rectangle class'''


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
        self.__height = val

    @property
    def x(self):
        '''x getter'''
        return self.__x

    @x.setter
    def x(self, val):
        '''x setter'''
        if type(val) is not int:
            raise TypeError('x must be an integer')
        if val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        '''y getter'''
        return self.__y

    @y.setter
    def y(self, val):
        '''y setter'''
        if type(val) is not int:
            raise TypeError('y must be an integer')
        if val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        '''rets area of the rectangle'''
        return self.width * self.height

    def display(self):
        '''displays a rect'''
        rect = self.y * '\n'
        for idx in range(self.height):
            rect += (' ' * self.x)
            rect += ('#' * self.width) + '\n'

        print(rect, end='')

    def __str__(self):
        '''str method'''
        str_rect = '[Rectangle] '
        str_id = f'({self.id}) '
        str_xy = f'{self.x}/{self.y} - '
        str_wh = f'{self.width}/{self.height}'

        return str_rect + str_id + str_xy + str_wh

    def update(self, *args, **kwargs):
        '''update method'''
        if args is not None and len(args) != 0:
            ls_atr = ['id', 'width', 'height', 'x', 'y']
            for idx in range(len(args)):
                setattr(self, ls_str[idx], args[idx])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        '''method to ret a dict with properties'''
        ls_atr = ['id', 'width', 'height', 'x', 'y']
        d_res = {}

        for key in ls_atr:
            d_res[key] = getattr(self, key)

        return d_res
