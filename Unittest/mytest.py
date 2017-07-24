import unittest


def add(a, b):
    return a + b


def sub(a, b):
    return a -b


class MyTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(8, add(5, 3))

    def test_sub(self):
        self.assertEqual(2, sub(6, 4))


if __name__ == '__main__':
    unittest.main()