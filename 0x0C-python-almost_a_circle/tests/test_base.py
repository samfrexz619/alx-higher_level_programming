#!/usr/bin/python3
'''Module for test Base class'''

import unittest
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
from io import StringIO
from unittest import TestCase
from unittest.mock import patch


class TestBaseMethods(unittest.TestCase):
    '''Suite to test Base class'''

    def set_up(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Testing assigned id """
        nw = Base(1)
        self.assertEqual(nw.id, 1)

    def test_id_default(self):
        """ Testing default id """
        nw = Base()
        self.assertEqual(nw.id, 1)

    def test_id_nb_objects(self):
        """ Testing nb object attribute """
        nw = Base()
        nw2 = Base()
        nw3 = Base()
        self.assertEqual(nw.id, 1)
        self.assertEqual(nw2.id, 2)
        self.assertEqual(nw3.id, 3)

    def test_id_mix(self):
        """ Testing nb object attributes and assigned id """
        nw = Base()
        nw2 = Base(1024)
        nw3 = Base()
        self.assertEqual(nw.id, 1)
        self.assertEqual(nw2.id, 1024)
        self.assertEqual(nw3.id, 2)

    def test_string_id(self):
        """ Testing str id """
        nw = Base('1')
        self.assertEqual(nw.id, '1')

    def test_more_args_id(self):
        """ Test passing more args to init method """
        with self.assertRaises(TypeError):
            nw = Base(1, 1)

    def test_access_private_attrs(self):
        """ Test accessing to private attrs """
        nw = Base()
        with self.assertRaises(AttributeError):
            nw.__nb_objects

    def test_save_to_file_1(self):
        """ Test JSON file """
        Square.save_to_file_csv(None)
        res = "[]\n"
        with open("Square.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)

        try:
            os.remove("Square.json")
        except:
            pass

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_2(self):
        """ Test JSON file """
        Rectangle.save_to_file_csv(None)
        res = "[]\n"
        with open("Rectangle.json", "r") as file:
            with patch('sys.stdout', new=StringIO()) as str_out:
                print(file.read())
                self.assertEqual(str_out.getvalue(), res)
        try:
            os.remove("Rectangle.json")
        except:
            pass

        Rectangle.save_to_file_csv([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), "[]")
