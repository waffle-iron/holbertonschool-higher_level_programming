#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_list_with_only_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    def test_list_with_not_an_int(self):
        with self.assertRaises(TypeError):
            max_integer(['a', 2, 3, 4])

if __name__ == '__main__':
    unittest.main(exit=False)
