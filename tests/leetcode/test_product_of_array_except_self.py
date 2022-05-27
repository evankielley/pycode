import unittest
from leetcode.product_of_array_except_self import f


class Test(unittest.TestCase):
    def setUp(self):
        self.f = f
    def test_1(self):
        self.assertEqual(f([1,2,3,4]), [24,12,8,6])
    def test_2(self):
        self.assertEqual(f([-1,1,0,-3,3]), [0,0,9,0,0])
