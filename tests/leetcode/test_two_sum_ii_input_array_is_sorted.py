import unittest
from leetcode.two_sum_ii_input_array_is_sorted import f


class Test(unittest.TestCase):
    def setUp(self):
        self.f = f
    def test_1(self):
        self.assertListEqual(self.f([2,7,11,15], 9), [1,2])
    def test_2(self):
        self.assertListEqual(self.f([2,3,4], 6), [1,3])
    def test_3(self):
        self.assertListEqual(self.f([-1,0], -1), [1,2])
