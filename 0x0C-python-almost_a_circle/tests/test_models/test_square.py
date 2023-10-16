#!/usr/bin/python3
"""Defining the test module for 'models.square.py'"""

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base

import unittest


class TestSquare(unittest.TestCase):
    """Unittests for testing cases of the Square class"""

    # Reseting the id
    def setUp(self):
        Base._Base__nb_objects = 0

    # Testing Inheritance
    def test_inheritance(self):
        s = Square(2)
        self.assertTrue(isinstance(s, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    # testing instantiating
    def test_constructor(self):
        s = Square(2)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_constructor_all(self):
        s = Square(2, 1, 3, 89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_constructor_check_width_height(self):
        s = Square(2, 1, 3, 89)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.width, 2)
        self.assertEqual(s.height, 2)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 3)

    def test_invalid_size_type(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("4")

    def test_invalid_size_valuee(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def test_no_args(self):
        with self.assertRaises(TypeError) as x:
            s = Square()

    # testing 'str()'
    def test_str(self):
        def test_str(self):
            s = Square(2)
            expected = f"[Square] (1) 0/0 - 2"
            self.assertEqual(expected, r.__str__())

    def test_str_all(self):
        def test_str(self):
            s = Square(2, 3, 4, 89)
            expected = f"[Square] (89) 3/4 - 2"
            self.assertEqual(expected, r.__str__())

    # Testing Update
    def test_update_args_kwargs(self):
        s = Square(2)
        args = [89, 4, 6, 7]
        kw = {"id": 99, "size": 10, "x": 30, "y": 40}
        s.update(*args, **kw)
        self.assertEqual("[Square] (89) 6/7 - 4", str(s))

    def test_update_kwargs(self):
        s = Square(2)
        args = []
        kw = {"id": 89, "size": 10, "x": 30, "y": 40}
        s.update(*args, **kw)
        self.assertEqual("[Square] (89) 30/40 - 10", str(s))

    def test_update_empty(self):
        s = Square(2)
        args = []
        kw = {}
        s.update(*args, **kw)
        self.assertEqual("[Square] (1) 0/0 - 2", str(s))

    def test_update_args_more(self):
        s = Square(2)
        args = [89, 4, 6, 7, 0, 0]
        kw = {}
        s.update(*args, **kw)
        self.assertEqual("[Square] (89) 6/7 - 4", str(s))

    def test_update_args_invalid_width_type(self):
        s = Square(2)
        args = [89, '4', 6, 7]
        kw = {}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(*args, **kw)

    def test_update_kwargs_invalid_width_value(self):
        s = Square(2)
        args = []
        kw = {"id": 89, "size": 0, "x": 30, "y": 40}
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.update(*args, **kw)


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing 'to_dictionary' method of the Square class."""

    # Reset the __nb_objects attribute before each test, to avoid interferences
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_to_dictionary(self):
        s = Square(2)
        expected = {'id': 1, 'size': 2, 'x': 0, 'y': 0}
        self.assertEqual(expected, s.to_dictionary())

    def test_to_dictionary_all(self):
        s = Square(2, 4, 5, 89)
        expected = {'id': 89, 'size': 2, 'x': 4, 'y': 5}
        self.assertEqual(expected, s.to_dictionary())

    def test_to_dictionary_arg(self):
        s = Square(2)
        with self.assertRaises(TypeError):
            s.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
