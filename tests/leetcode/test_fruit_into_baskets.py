import unittest
from leetcode.fruit_into_baskets import f

class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertEqual(self.f([1,2,1]), 3)

    def test_two(self):
        self.assertEqual(self.f([0,1,2,2]), 3)

    def test_three(self):
        self.assertEqual(self.f([1,2,3,2,2]), 4)

    def test_four(self):
        self.assertEqual(self.f([3,3,3,1,2,1,1,2,3,3,4]), 5)
