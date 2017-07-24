import unittest
from coder import Coder


class CoderTestCase(unittest.TestCase):
    # def test_skill_in(self):
    #     c = Coder('tom')
    #     c.mastering_skill('python')
    #     c.mastering_skill('ASP.NET MVC')
    #
    #     self.assertIn('python', c.skills)

    def setUp(self):
        self.c = Coder('tom')
        self.c.skills = ['python', '.net']

    def test_skill_in(self):
        self.assertIn('python', self.c.skills)

if __name__ == '__main__':
    unittest.main()