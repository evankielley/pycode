import unittest
from leetcode.car_fleet import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertEqual(self.f(12, [10,8,0,5,3], [2,4,1,1,3]), 3)

    def test_two(self):
        self.assertEqual(self.f(10, [3], [3]), 1)

    def test_three(self):
        self.assertEqual(self.f(100, [0,2,4], [4,2,1]), 1)
