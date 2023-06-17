#!/usr/bin/python3
'''module that contains the base class'''


class Base:
    '''class Base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init instance'''
        self.id = id

        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def 
