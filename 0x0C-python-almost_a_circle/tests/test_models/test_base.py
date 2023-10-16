#!/usr/bin/python3
"""Defining the unittests for the 'Base' class"""

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_initialization_with_id(self):
        obj = Base(5)
        self.assertEqual(obj.id, 5)

    def test_initialization_without_id(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(Base._Base__nb_objects, 2)

    def test_id_not_int(self):
        b = Base("109")
        self.assertEqual("109", b.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """Unittests for testing to_json_string method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_json_rectanlge(self):
        r = Rectangle(2, 3, 4, 5, 12)
        json_dict = r.to_dictionary()
        json_str = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_str),
                         [{'id': 12, 'width': 2, 'height': 3, 'x': 4, 'y': 5}])

    def test_to_json_squares(self):
        s = Square(2)
        s2 = Square(3, 4, 5)
        json_dict_1 = s.to_dictionary()
        json_dict_2 = s2.to_dictionary()
        json_str = Base.to_json_string([json_dict_1, json_dict_2])
        expected = [json_dict_1, json_dict_2]
        self.assertEqual(json.loads(json_str), expected)

    def test_to_json_empty(self):
        json_str = Base.to_json_string([])
        self.assertEqual(json.loads(json_str), [])

    def test_to_json_None(self):
        json_str = Base.to_json_string(None)
        self.assertEqual(json.loads(json_str), [])


class TestBase_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file(self):
        r = Rectangle(2, 3, 1, 0, 89)
        Rectangle.save_to_file([r])
        expected = [r.to_dictionary()]
        with open("Rectangle.json", "r") as f:
            self.assertEqual(json.loads(f.read()), expected)

    def test_save_to_file_square(self):
        s = Square(3)
        s2 = Square(4)
        Square.save_to_file([s, s2])
        expected = [s.to_dictionary(), s2.to_dictionary()]
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), expected)

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [])

    def test_save_to_file_empty(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [])


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing 'from_json_string' method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_from_json_string_rectangle(self):
        r = Rectangle(2, 3)
        list_input = [r.to_dictionary()]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_squares(self):
        s = Square(2)
        s2 = Square(3)
        list_input = [s.to_dictionary(), s2.to_dictionary()]
        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string(""))


class TestBase_create(unittest.TestCase):
    """Unittests for testing 'create' method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_rectangle(self):
        r = Rectangle(2, 3)
        obj = Rectangle.create(**(r.to_dictionary()))
        self.assertEqual(str(r), str(obj))

    def test_create_square_is(self):
        r = Rectangle(2, 3)
        obj = Rectangle.create(**(r.to_dictionary()))
        self.assertIsNot(r, obj)

    def test_create_rectangle_not_equal(self):
        r = Rectangle(2, 3)
        obj = Rectangle.create(**(r.to_dictionary()))
        self.assertNotEqual(r, obj)

    def test_create_square(self):
        s = Square(2)
        obj = Square.create(**(s.to_dictionary()))
        self.assertEqual(str(s), str(obj))


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing 'load_from_file_method' of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_load_from_file_rectangle(self):
        r = Rectangle(2, 3)
        Rectangle.save_to_file([r])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(str(r), str(list_objs[0]))

    def test_load_from_file_type(self):
        r = Rectangle(2, 3)
        Rectangle.save_to_file([r])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(type(r), type(list_objs[0]))

    def test_load_from_file_rectangles(self):
        r = Rectangle(2, 3)
        r2 = Rectangle(5, 6)
        Rectangle.save_to_file([r, r2])
        list_objs = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_objs[1]))

    def test_load_from_file_Squares(self):
        s = Square(2)
        s2 = Square(5)
        Square.save_to_file([s, s2])
        list_objs = Square.load_from_file()
        self.assertEqual(str(s), str(list_objs[0]))

    def test_load_from_file_square_type(self):
        s = Square(2)
        Square.save_to_file([s])
        list_objs = Square.load_from_file()
        self.assertEqual(type(s), type(list_objs[0]))

    def test_load_from_file_no_file(self):
        self.assertEqual([], Base.load_from_file())


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file_csv_rectangle(self):
        r = Rectangle(2, 3)
        Rectangle.save_to_file_csv([r])
        header = "id,width,height,x,y\n"
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(header + "1,2,3,0,0\n", f.read())

    def test_save_to_file_csv_rectangles(self):
        r = Rectangle(2, 3)
        r2 = Rectangle(4, 5, 6, 7)
        Rectangle.save_to_file_csv([r, r2])
        header = "id,width,height,x,y\n"
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(header + "1,2,3,0,0\n" + "2,4,5,6,7\n", f.read())

    def test_save_to_file_csv_rectangles(self):
        s = Square(2)
        s2 = Square(4)
        Square.save_to_file_csv([s, s2])
        header = "id,size,x,y\n"
        with open("Square.csv", "r") as f:
            self.assertEqual(header + "1,2,0,0\n" + "2,4,0,0\n", f.read())

    def test_save_to_file_csv_empty(self):
        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_csv_none(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            self.assertEqual("[]", f.read())


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing 'load_from_file_csv' method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_load_from_file_csv_first_rectangles(self):
        r = Rectangle(3, 4)
        r2 = Rectangle(5, 6)
        Rectangle.save_to_file_csv([r, r2])
        list_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_output[1]))

    def test_load_from_file_csv_first_Squares(self):
        s = Square(3)
        s2 = Square(5)
        Square.save_to_file_csv([s, s2])
        list_output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(list_output[1]))

    def test_load_from_file_csv_no_file(self):
        output = Base.load_from_file_csv()
        self.assertEqual([], output)


if __name__ == '__main__':
    unittest.main()
