import unittest
from leetcode.generate_parentheses import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertCountEqual(self.f(3), ["((()))","(()())","(())()","()(())","()()()"])

    def test_two(self):
        self.assertCountEqual(self.f(1), ["()"])
