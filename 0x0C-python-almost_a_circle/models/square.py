#!/usr/bin/python3
'''module that contains class Square'''

from models.rectangle import Rectangle

''''sqaure class'''


class Square(Rectangle):
    '''class square'''

    def __init__(self, size, x=0, y=0, id=None):
        '''init instances'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str method'''
        str_squ = '[Square] '
        str_id = f'({self.id}) '
        str_xy = f'{self.x}/{self.y} - '
        str_wh = f'{self.width}/{self.height}'

        return str_squ + str_id + str_xy + str_wh

    @property
    def size(self):
        '''getter size'''
        return self.width

    @size.setter
    def size(self, val):
        '''setter size'''
        self.width = val
        self.height = val

    def __str__(self):
        '''str method'''
        str_rect = '[Square] '
        str_id = f'({self.id}) '
        str_xy = f'{self.x}/{self.y} - '
        str_sz = f'{self.size}'
        return str_rect + str_id + str_xy + str_sz

    def update(self, *args, **kwargs):
        '''update method'''
        if args is not None and len(args) != 0:
            ls_atr = ['id', 'size', 'x', 'y']
            for idx in range(len(args)):
                if ls_atr[idx] == 'size':
                    setattr(self, 'width', args[idx])
                    setattr(self, 'height', args[idx])
                else:
                    setattr(self, ls_atr[idx], args[idx])

        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        '''returns a dictionary with it attr'''
        ls_atr = ['id', 'size', 'x', 'y']
        d_res = {}

        for key in ls_atr:
            if key == 'size':
                d_res[key] = getattr(self, 'width')
            else:
                d_res[key] = getattr(self, key)

        return d_res
