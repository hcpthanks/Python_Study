import unittest


person = {'name': 'mike', 'age':20}
numbers = [1, 3, 2, 88, 7, 44]
s = 'hcpthanks  git@github.com'


class TestAssert(unittest.TestCase):
    def test_assert_method(self):
        # self.assertEqual('mike', person.get('name'))
        # self.assertTrue('有品课堂' in s)
        # self.assertIn('hcpthanks', s)
        # self.assertAlmostEqual(3.3, 1.1+2.2)
        # self.assertIs(True + 1, 2)
        self.assertIsInstance(s, str)
        self.assertGreater(7, numbers[0])

if __name__ == '__main__':
    unittest.main()
