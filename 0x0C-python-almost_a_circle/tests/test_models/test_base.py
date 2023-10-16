#!/usr/bin/python3
""" Unittest for Base module """

import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_instantiation(unittest.TestCase):
    """ Unittest for testing instantiation of the Base class"""
    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id(self):
        obj = Base(5)
        self.assertEqual(5, obj.id)

    def test_id_none(self):
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(1, obj1.id)
        self.assertEqual(2, obj2.id)
        self.assertEqual(2, Base._Base__nb_objects)

    def test_id_not_int(self):
        obj = Base("base")
        self.assertEqual("base", obj.id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBase_to_json_string(unittest.TestCase):
    """ Unittests for testing to_json_string method of Base class """

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_none_list(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_more_than_one_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([], 120)

    def test_non_empty_list(self):
        data = [{"key1": "value1", "key2": "value2"}]
        result = Base.to_json_string(data)
        self.assertEqual(result, json.dumps(data))

    def test_nested_list(self):
        nested_data = [{"key1": "value1", "key2": [1, 2, 3]}]
        result = Base.to_json_string(nested_data)
        self.assertEqual(result, json.dumps(nested_data))


class TestBase_save_to_file(unittest.TestCase):
    """ Unittests for testing save_to_file method of Base class """

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file_one_rectangle(self):
        r = Rectangle(2, 4)
        Rectangle.save_to_file([r])
        text = '[{"id": 1, "width": 2, "height": 4, "x": 0, "y": 0}]'
        with open("Rectangle.json", "r") as file:
            self.assertEqual(file.read(), text)

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()


class TestBase_from_json_string(unittest.TestCase):
    """Unittests for testing from_json_string method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_from_json_string_one_rectangle(self):
        list_input = [{"id": 89, "width": 10, "height": 4, "x": 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_two_rectangles(self):
        list_input = [
             {'id': 89, 'width': 10, 'height': 4},
             {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_input, list_output)

    def test_from_json_string_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestBase_create(unittest.TestCase):
    """Unittests for testing create method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_create_rectangle_original(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r1))

    def test_create_rectangle_new(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual("[Rectangle] (7) 1/2 - 3/5", str(r2))

    def test_create_rectangle_is(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_create_rectangle_equals(self):
        r1 = Rectangle(3, 5, 1, 2, 7)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)


class TestBase_load_from_file(unittest.TestCase):
    """Unittests for testing load_from_file_method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_load_from_file_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file([r1, r2])
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))


class TestBase_save_to_file_csv(unittest.TestCase):
    """Unittests for testing save_to_file_csv method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_save_to_file_csv_one_rectangle(self):
        r = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as file:
            self.assertEqual("id,width,height,x,y\n5,10,7,2,8\n", file.read())

    def test_save_to_file_csv_one_square(self):
        s = Square(10, 7, 2, 8)
        Square.save_to_file_csv([s])
        with open("Square.csv", "r") as file:
            self.assertEqual("id,size,x,y\n8,10,7,2\n", file.read())

    def test_save_to_file__csv_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", "r") as file:
            self.assertEqual("[]", file.read())

    def test_save_to_file_csv_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unittests for testing load_from_file_csv method of Base class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_load_from_file_csv_first_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(list_rectangles_output[0]))

    def test_load_from_file_csv_second_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 1)
        r2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([r1, r2])
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(list_rectangles_output[1]))

    def test_load_from_file_csv_no_file(self):
        output = Base.load_from_file_csv()
        self.assertEqual([], output)


if __name__ == "__main__":
    unittest.main()
