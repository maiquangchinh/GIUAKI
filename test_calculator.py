# test_calculator.py

import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.cal = Calculator()

    def test_add(self):
        self.assertEqual(self.cal.add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(self.cal.subtract(4, 3), 1)

    def test_multiply(self):
        self.assertEqual(self.cal.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.cal.divide(6, 3), 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.cal.divide(5, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

if __name__ == '__main__':
    unittest.main()
