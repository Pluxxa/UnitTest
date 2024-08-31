import unittest
from main import remainder

import unittest

class TestRemainderFunction(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(remainder(10, 3), 1)
        self.assertEqual(remainder(20, 5), 0)
        self.assertEqual(remainder(15, 4), 3)

    def test_negative_numbers(self):
        self.assertEqual(remainder(-10, 3), 2)
        self.assertEqual(remainder(10, -3), -2)
        self.assertEqual(remainder(-10, -3), -1)

    def test_zero_dividend(self):
        self.assertEqual(remainder(0, 3), 0)
        self.assertEqual(remainder(0, -3), 0)

    def test_zero_divisor(self):
        with self.assertRaises(ValueError):
            remainder(10, 0)

    def test_large_numbers(self):
        self.assertEqual(remainder(123456789012345, 123456789), 12345)

if __name__ == '__main__':
    unittest.main()
