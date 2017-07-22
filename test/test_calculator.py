import unittest
from calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.c = Calculator(5, 3)

    def test_add(self):
        self.assertEqual(8, self.c.add())

    def test_subtract(self):
        self.assertEqual(2, self.c.subtract())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()