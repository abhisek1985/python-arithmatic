import unittest
from arithmatic.arithmatic import (
    addition, multiplication, subtraction, division, floor_division, power)
import sys


class TestArithmatic(unittest.TestCase):
    def setUp(self):
        self.python_version = sys.version_info[0]

    def test_addition_with_value(self):
        self.assertEqual(addition(2, 3), 5)

    def test_addition_without_value(self):
        self.assertEqual(addition(), None)

    def test_subtraction_with_value(self):
        self.assertEqual(subtraction(5, 3), 2)

    def tes_subtraction_without_value(self):
        self.assertIsNone(subtraction())

    def test_multiplication_with_value(self):
        self.assertEqual(multiplication(10, 50), 500)

    def test_multiplication_without_value(self):
        self.assertIsNone(multiplication())

    def test_division_with_value(self):
        if self.python_version == 3:
            self.assertEqual(division(10, 3), 3.3333333333333335)
        else:
            self.assertEqual(division(10, 3), 3)

    def test_division_without_value(self):
        self.assertIsNone(division())

    def test_floor_division_with_value(self):
        self.assertEqual(floor_division(5, 2), 2)

    def test_floor_division_without_value(self):
        self.assertIsNone(floor_division())

    def test_power_with_value(self):
        self.assertEqual(power(2, 3), 8)

    def test_power_without_value(self):
        self.assertIsNone(power())


if __name__ == '__main__':
    unittest.main()
