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

    def to_json(self):
        '''method to json'''
        return self.__dict__
