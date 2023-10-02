#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defining the 'TestMaxInteger' class"""

    def test_1(self):
        my_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(my_list), 4)

    def test_2(self):
        my_list = [1, 2, 4, 3]
        self.assertEqual(max_integer(my_list), 4)

    def test_3(self):
        my_list = [4, 3, 1, 3]
        self.assertEqual(max_integer(my_list), 4)

    def test_3(self):
        my_list = [1]
        self.assertEqual(max_integer(my_list), 1)

    def test_4(self):
        my_list = [-1, 1, 0]
        self.assertEqual(max_integer(my_list), 1)

    def test_5(self):
        my_list = []
        self.assertEqual(max_integer(my_list), None)

    def test_6(self):
        my_list = [1.2, 0.1, 5.7, 4.3, -7.7]
        self.assertEqual(max_integer(my_list), 5.7)

    def test_66(self):
        my_list = [1.2, 1, 5.7, 4.3, -7]
        self.assertEqual(max_integer(my_list), 5.7)

    def test_7(self):
        my_list = ['e', 'd', 'x', 'g', '99']
        self.assertEqual(max_integer(my_list), 'x')

    def test_8(self):
        my_list = ['abd', 'azx', '99']
        self.assertEqual(max_integer(my_list), 'azx')

    def test_9(self):
        my_list = "Ali"
        self.assertEqual(max_integer(my_list), 'l')


if __name__ == '__main__':
    unittest.main()
