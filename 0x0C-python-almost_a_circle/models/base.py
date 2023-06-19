#!/usr/bin/python3
'''module that contains the base class'''

import json
import csv
import os.path

'''base class'''


class Base:
    '''class Base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''init instance'''

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''method that ret json str'''
        if list_dictionaries is None or list_dictionaries == '[]':
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''save obj in a file'''
        f_name = f'{cls.__name__}.json'
        ls_dic = []

        if not list_objs:
            pass
        else:
            for idx in range(len(list_objs)):
                ls_dic.append(list_objs[idx].to_dictionary())

        ls = cls.to_json_string(ls_dic)

        with open(f_name, 'w') as f:
            f.write(ls)

    @staticmethod
    def from_json_string(json_string):
        '''json str to dict'''
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''create an instance'''
        if cls.__name__ == 'Rectangle':
            nw = cls(10, 10)
        else:
            nw = cls(10)
        nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file_csv(cls):
        '''ret a list of instance'''
        f_name = f'{cls.__name__}.json'

        if os.path.exists(f_name) is False:
            return []

        with open(f_name, 'r') as f:
            ls_str = f.read()

        ls_cls = cls.from_json_string(ls_str)
        ls_ins = []

        for idx in range(len(ls_cls)):
            ls_ins.append(cls.create(**ls_cls[idx]))

        return ls_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''method to save a csv file'''
        f_name = f'{cls.__name__}.csv'

        if cls.__name__ == 'Rectangle':
            ls_dict = [0, 0, 0, 0, 0]
            ls_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            ls_dict = ['0', '0', '0', '0']
            ls_keys = ['id', 'size', 'x', 'y']

        matx = []

        if not list_objs:
            pass

        else:
            for ob in list_objs:
                for ky in range(len(ls_keys)):
                    ls_dict[ky] = ob.to_dictionary()[ls_keys[ky]]
                matx.append(ls_dict[:])

        with open(f_name, 'w') as wFile:
            writer = csv.writer(wFile)
            writer.writerows(matx)
