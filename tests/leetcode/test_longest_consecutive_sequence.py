import unittest
from leetcode.longest_consecutive_sequence import f


class Test(unittest.TestCase):
    def setUp(self):
        self.f = f
    def test_1(self):
        self.assertEqual(self.f([100,4,200,1,3,2]), 4)
    def test_2(self):
        self.assertEqual(self.f([0,3,7,2,5,8,4,6,0,1]), 9)
    def test_3(self):
        self.assertEqual(self.f([]), 0)
