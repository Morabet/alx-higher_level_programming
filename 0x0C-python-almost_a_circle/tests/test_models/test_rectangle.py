#!/usr/bin/python3
"""Defining unittests for 'models/rectangle.py'."""

from models.base import Base
from models.rectangle import Rectangle

import unittest


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_constructor(self):
        rect = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rect.id, 10)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_constructor_no_id_two_args(self):
        rect = Rectangle(4, 5)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 4)
        self.assertEqual(rect.height, 5)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle("4", 5, 1, 2)

    def test_invalid_width_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5, 1, 2)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(4, "5", 1, 2)

    def test_invalid_height_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 0, 1, 2)

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 5, "1", 2)

    def test_invalid_x_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -1, 2)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            rect = Rectangle(4, 5, 1, "2")

    def test_invalid_y_value(self):
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 1, -2)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(5, 5, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.width)

    def test_width_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.height)

    def test_height_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Rectangle(5, 7, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestRectangle_area(unittest.TestCase):
    """testing the 'area' function"""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_area(self):
        r = Rectangle(4, 3)
        self.assertEqual(12, r.area())

    def test_area_after_change(self):
        r = Rectangle(4, 3)
        r.width = 5
        r.height = 4
        self.assertEqual(20, r.area())

    def test_passing_arg(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.area(2)


class TestRectangle_str(unittest.TestCase):
    """testing the '__str__' method"""

    def test_str(self):
        r = Rectangle(2, 3)
        expected = f"[Rectangle] ({r.id}) {r.x}/{r.y} - "
        expected += f"{r.width}/{r.height}"
        self.assertEqual(expected, r.__str__())

    def test_str_x_y(self):
        r = Rectangle(2, 3, 6, 7, 12)
        expected = f"[Rectangle] (12) 6/7 - "
        expected += f"2/3"
        self.assertEqual(expected, r.__str__())


class TestRectangle_update_args(unittest.TestCase):
    """testing the 'update' function"""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    # Testing '*args'
    def test_update_id(self):
        r = Rectangle(2, 3)
        r.update(12)
        self.assertEqual(12, r.id)

    def test_update_all(self):
        r = Rectangle(12, 2, 3, 4, 5)
        r.update(1, 6, 7, 3, 2)
        self.assertEqual("[Rectangle] (1) 3/2 - 6/7", str(r))

    def test_update_w_h(self):
        r = Rectangle(2, 3)
        r.update(1, 6, 7)
        self.assertEqual("[Rectangle] (1) 0/0 - 6/7", str(r))

    def test_update_x_y(self):
        r = Rectangle(2, 3)
        r.update(1, 1, 1, 6, 7)
        self.assertEqual("[Rectangle] (1) 6/7 - 1/1", str(r))

    def test_update_no_id(self):
        r = Rectangle(12, 2, 3, 4, 5)
        r.update(None, 6, 7, 3, 2)
        self.assertEqual("[Rectangle] (5) 3/2 - 6/7", str(r))

    def test_update_twice(self):
        r = Rectangle(2, 3)
        r.update(None, 6, 7, 3, 2)
        r.update(99, 5, 8, 2, 1)
        self.assertEqual("[Rectangle] (99) 2/1 - 5/8", str(r))

    def test_update_args_invalid_width_type(self):
        r = Rectangle(2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(89, "invalid")

    def test_update_args_invalid_width_value(self):
        r = Rectangle(2, 3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(89, 0)

    # Testing '**kwargs'
    def test_update_kwargs_id(self):
        r = Rectangle(2, 3)
        kw = {"id": 89}
        r.update(**kw)
        self.assertEqual("[Rectangle] (89) 0/0 - 2/3", str(r))

    def test_update_kwargs_no_id(self):
        r = Rectangle(2, 3, 1, 1, 12)
        kw = {"id": None}
        r.update(**kw)
        self.assertEqual("[Rectangle] (12) 1/1 - 2/3", str(r))

    def test_update_kwargs_all(self):
        r = Rectangle(2, 3)
        kw = {"id": 89, "width": 4, "height": 5, "x": 6, "y": 7}
        r.update(**kw)
        self.assertEqual("[Rectangle] (89) 6/7 - 4/5", str(r))

    def test_update_kwargs_all_not_ordered(self):
        r = Rectangle(2, 3)
        kw = {"x": 6, "y": 7, "height": 5, "id": 89, "width": 4}
        r.update(**kw)
        self.assertEqual("[Rectangle] (89) 6/7 - 4/5", str(r))

    def test_update_kwargs_not_all(self):
        r = Rectangle(2, 3)
        kw = {"id": 89, "width": 4, "x": 6}
        r.update(**kw)
        self.assertEqual("[Rectangle] (89) 6/0 - 4/3", str(r))

    def test_update_kwargs_invalid_width_type(self):
        r = Rectangle(2, 3)
        kw = {"id": 89, "width": '4', "x": 6}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(**kw)

    def test_update_kwargs_invalid_width_value(self):
        r = Rectangle(2, 3)
        kw = {"id": 89, "width": 0, "x": 6}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(**kw)

    # Test: '*args' and '**kwargs'
    def test_update_args_kwargs(self):
        r = Rectangle(2, 3)
        args = [89, 4, 5, 6, 7]
        kw = {"id": 99, "width": 10, "height": 20, "x": 30, "y": 40}
        r.update(*args, **kw)
        self.assertEqual("[Rectangle] (89) 6/7 - 4/5", str(r))

    def test_update_empty_args(self):
        r = Rectangle(2, 3)
        args = []
        kw = {"id": 99, "width": 10, "height": 20, "x": 30, "y": 40}
        r.update(*args, **kw)
        self.assertEqual("[Rectangle] (99) 30/40 - 10/20", str(r))

    def test_update_empty_kwargs(self):
        r = Rectangle(2, 3)
        args = [89, 4, 5, 6, 7]
        kw = {}
        r.update(*args, **kw)
        self.assertEqual("[Rectangle] (89) 6/7 - 4/5", str(r))

    def test_update_empty(self):
        r = Rectangle(2, 3)
        args = []
        kw = {}
        r.update(*args, **kw)
        self.assertEqual("[Rectangle] (1) 0/0 - 2/3", str(r))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing 'to_dictionary' method of the Rectangle class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        r = Rectangle(2, 3)
        expected = {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0}
        self.assertEqual(expected, r.to_dictionary())

    def test_to_dictionary_all(self):
        r = Rectangle(2, 3, 6, 7, 89)
        expected = {'id': 89, 'width': 2, 'height': 3, 'x': 6, 'y': 7}
        self.assertEqual(expected, r.to_dictionary())

    def test_to_dictionary(self):
        r = Rectangle(2, 3)
        r2 = Rectangle(6, 7)
        self.assertNotEqual(r.to_dictionary(), r2.to_dictionary())

    def test_to_dictionary_arg(self):
        r = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
