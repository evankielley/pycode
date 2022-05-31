import unittest
from leetcode.container_with_most_water import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertEqual(self.f([1,8,6,2,5,4,8,3,7]), 49)

    def test_two(self):
        self.assertEqual(self.f([1,1]), 1)
