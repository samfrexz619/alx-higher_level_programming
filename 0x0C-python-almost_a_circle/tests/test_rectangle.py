#!/usr/bin/python3
'''module for test Rectangle class'''

import unittest
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleMethod(unittest.TestCase):
    '''suite to test Rectangle class'''

    def set_up(self):
        '''Method invoked for each test'''
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        '''Test new rectangle'''
        nw = Rectangle(1, 1)
        self.assertEqual(nw.width, 1)
        self.assertEqual(nw.height, 1)
        self.assertEqual(nw.x, 0)
        self.assertEqual(nw.y, 0)
        self.assertEqual(nw.id, 1)

    def test_new_rectangle_two(self):
        '''Test new rectangle with all attrs'''
        nw = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(nw.width, 2)
        self.assertEqual(nw.height, 3)
        self.assertEqual(nw.x, 5)
        self.assertEqual(nw.y, 5)
        self.assertEqual(nw.id, 4)

    def test_new_rectangles(self):
        '''Test new rectangles'''
        nw = Rectangle(1, 1)
        nw2 = Rectangle(1, 1)
        self.assertEqual(False, nw is nw2)
        self.assertEqual(False, nw.id == nw2.id)

    def test_is_Base_instance(self):
        '''Test Rectangle is a Base instance'''
        nw = Rectangle(1, 1)
        self.assertEqual(True, isinstance(nw, Base))

    def test_incorrect_amount_attrs(self):
        '''Test error raise with 1 arg passed'''
        with self.assertRaises(TypeError):
            nw = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        ''' Test error raised with no args passed'''
        with self.assertRaises(TypeError):
            nw = Rectangle()

    def test_access_private_attrs(self):
        '''Trying to access to a private attribute'''
        nw = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            nw.__width

    def test_access_private_attrs_two(self):
        '''Trying to access to a private attribute'''
        nw = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            nw.__height

    def test_access_private_attrs_three(self):
        '''Trying to access to a private attribute'''
        nw = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            nw.__x

    def test_access_private_attrs_four(self):
        '''Trying to access to a private attribute'''
        nw = Rectangle(1, 1)
        with self.assertRaises(AttributeError):
            nw.__y

    def test_valide_attrs(self):
        '''Trying to pass a str val'''
        with self.assertRaises(TypeError):
            nw = Rectangle("2", 2, 2, 2, 2)

    def test_valide_attrs_2(self):
        '''Trying to pass a str val'''
        with self.assertRaises(TypeError):
            nw = Rectangle(2, "2", 2, 2, 2)

    def test_valide_attrs_3(self):
        '''Trying to pass a str val'''
        with self.assertRaises(TypeError):
            nw = Rectangle(2, 2, "2", 2, 2)

    def test_valide_attrs_4(self):
        '''Trying to pass a str val'''
        with self.assertRaises(TypeError):
            nw = Rectangle(2, 2, 2, "2", 2)

    def test_value_attrs(self):
        '''Trying to pass invalid val'''
        with self.assertRaises(ValueError):
            nw = Rectangle(0, 1)

    def test_value_attrs_1(self):
        '''Trying to pass invalid val'''
        with self.assertRaises(ValueError):
            nw = Rectangle(1, 0)

    def test_value_attrs_2(self):
        '''Trying to pass invalid val'''
        with self.assertRaises(ValueError):
            nw = Rectangle(1, 1, -1)

    def test_value_attrs_3(self):
        '''Trying to pass invalid val'''
        with self.assertRaises(ValueError):
            nw = Rectangle(1, 1, 1, -1)

    def test_area(self):
        '''Check the return value of area method'''
        nw = Rectangle(4, 5)
        self.assertEqual(nw.area(), 20)

    def test_area_2(self):
        '''Check the return value of area method'''
        nw = Rectangle(2, 2)
        self.assertEqual(nw.area(), 4)
        nw.width = 5
        self.assertEqual(nw.area(), 10)
        nw.height = 5
        self.assertEqual(nw.area(), 25)

    def test_area_3(self):
        '''Check the return val of area method'''
        nw = Rectangle(3, 8)
        self.assertEqual(nw.area(), 24)
        nw2 = Rectangle(10, 10)
        self.assertEqual(nw2.area(), 100)

    def test_display(self):
        """ Test string printed """
        r1 = Rectangle(2, 5)
        res = "##\n##\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_2(self):
        """ Test string printed """
        r1 = Rectangle(2, 2)
        res = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.width = 5
        res = "#####\n#####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_str(self):
        """ Test __str__ return value """
        r1 = Rectangle(2, 5, 2, 4)
        res = "[Rectangle] (1) 2/4 - 2/5\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_2(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 2, 8, 8, 10)
        res = "[Rectangle] (10) 8/8 - 3/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r1.id = 1
        r1.width = 7
        r1.height = 15
        res = "[Rectangle] (1) 8/8 - 7/15\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_3(self):
        """ Test __str__ return value """
        r1 = Rectangle(5, 10)
        res = "[Rectangle] (1) 0/0 - 5/10\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(25, 86, 4, 7)
        res = "[Rectangle] (2) 4/7 - 25/86\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r3 = Rectangle(1, 1, 1, 1)
        res = "[Rectangle] (3) 1/1 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r3)
            self.assertEqual(str_out.getvalue(), res)

    def test_str_4(self):
        """ Test __str__ return value """
        r1 = Rectangle(3, 3)
        res = "[Rectangle] (1) 0/0 - 3/3"
        self.assertEqual(r1.__str__(), res)

    def test_display_3(self):
        """ Test string printed """
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_display_4(self):
        """ Test string printed """
        r1 = Rectangle(3, 2)
        res = "###\n###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.x = 4
        res = "    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

        r1.y = 2
        res = "\n\n    ###\n    ###\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary(self):
        """ Test dictionary returned """
        r1 = Rectangle(1, 2, 3, 4, 1)
        res = "[Rectangle] (1) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 1)

        res = "<class 'dict'>\n"

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1.to_dictionary()))
            self.assertEqual(str_out.getvalue(), res)

    def test_to_dictionary_2(self):
        """ Test dictionary returned """
        r1 = Rectangle(2, 2, 2, 2)
        res = "[Rectangle] (1) 2/2 - 2/2\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r1)
            self.assertEqual(str_out.getvalue(), res)

        r2 = Rectangle(5, 7)
        res = "[Rectangle] (2) 0/0 - 5/7\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(r2)
            self.assertEqual(str_out.getvalue(), res)

        r1_dictionary = r1.to_dictionary()
        r2.update(**r1_dictionary)

        self.assertEqual(r1.width, r2.width)
        self.assertEqual(r1.height, r2.height)
        self.assertEqual(r1.x, r2.x)
        self.assertEqual(r1.y, r2.y)
        self.assertEqual(r1.id, r2.id)

        res = "<class 'dict'>\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            print(type(r1_dictionary))
            self.assertEqual(str_out.getvalue(), res)

    def test_dict_to_json(self):
        """ Test Dictionary to JSON string """
        r1 = Rectangle(2, 2)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        res = "[{}]\n".format(dictionary.__str__())

        with patch('sys.stdout', new=StringIO()) as str_out:
            print(json_dictionary)
            self.assertEqual(str_out.getvalue(), res.replace("'", "\""))

    def test_check_value(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2)

    def test_check_value_2(self):
        """ Test args passed """
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, -2)

    def test_create(self):
        """ Test create method """
        dictionary = {'id': 89}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)

    def test_create_2(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)

    def test_create_3(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)

    def test_create_4(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)

    def test_create_5(self):
        """ Test create method """
        dictionary = {'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        r1 = Rectangle.create(**dictionary)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

    def test_load_from_file(self):
        """ Test load JSON file """
        load_file = Rectangle.load_from_file()
        self.assertEqual(load_file, [])

    def test_load_from_file_2(self):
        """ Test load JSON file """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(8, 2, 5, 5)

        lput = [r1, r2]
        Rectangle.save_to_file(lput)
        loutput = Rectangle.load_from_file()

        for idx in range(len(lput)):
            self.assertEqual(lput[idx].__str__(), loutput[idx].__str__())
