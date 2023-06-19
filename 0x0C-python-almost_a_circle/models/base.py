#!/usr/bin/python3
'''Module that contains class Base'''

import json
import csv
import os.path

'''base class'''


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        '''init instances'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Ls to JSON str'''
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Save obj in a file'''
        f_name = "{}.json".format(cls.__name__)
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
        '''Create an instance'''
        if cls.__name__ == 'Rectangle':
            nw = cls(10, 10)
        else:
            nw = cls(10)
        nw.update(**dictionary)
        return nw

    @classmethod
    def load_from_file(cls):
        '''Returns a list of instances'''
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
        '''method that saves a CSV file'''
        f_name = f'{cls.__name__}.csv'

        if cls.__name__ == "Rectangle":
            ls_dic = [0, 0, 0, 0, 0]
            ls_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            ls_dic = ['0', '0', '0', '0']
            ls_keys = ['id', 'size', 'x', 'y']

        matx = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for ky in range(len(ls_keys)):
                    ls_dic[ky] = obj.to_dictionary()[ls_keys[ky]]
                matx.append(ls_dic[:])

        with open(f_name, 'w') as wFile:
            writer = csv.writer(wFile)
            writer.writerows(matx)

    @classmethod
    def load_from_file_csv(cls):
        '''method that loads a CSV file'''
        f_name = f'{cls.__name__}.csv'

        if os.path.exists(f_name) is False:
            return []

        with open(f_name, 'r') as rFile:
            rdr = csv.reader(rFile)
            csv_ls = list(rdr)

        if cls.__name__ == 'Rectangle':
            ls_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            ls_keys = ['id', 'size', 'x', 'y']

        matx = []

        for elem in csv_ls:
            d_csv = {}
            for kv in enumerate(elem):
                d_csv[ls_keys[kv[0]]] = int(kv[1])
            matx.append(d_csv)

        ls_ins = []

        for idx in range(len(matx)):
            ls_ins.append(cls.create(**matx[idx]))

        return ls_ins
