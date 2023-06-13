#!/usr/bin/python3
'''module'''


class Student:
    '''student class'''

    def __init__(self, first_name, last_name, age):
        '''method to init

        Args:
            first_name: first
            last_name: last
            age: age

        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''method to json

        Arg:
            attr: list of str

        '''
        if type(attrs) is not list:
            return self.__dict__

        else:
            n_obj = {}
            obj = self.__dict__
            for idx in attrs:
                for e in obj:
                    if (idx == e):
                        n_obj[idx] = obj[idx]

            return n_obj
