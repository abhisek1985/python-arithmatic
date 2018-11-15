import unittest
from arithmatic.arithmatic import (
    addition, multiplication, subtraction, division, floor_division, power)


class TestArithmatic(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)

    def test_subtraction(self):
        self.assertEqual(subtraction(5, 3), 2)

    def test_multiplication(self):
        self.assertEqual(multiplication(10, 50), 500)

    def test_division(self):
        self.assertEqual(division(10, 3), 3.3333333333333335)

    def test_floor_division(self):
        self.assertEqual(floor_division(5, 2), 2)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)


if __name__ == '__main__':
    unittest.main()
