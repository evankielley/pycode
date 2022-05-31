import unittest
from leetcode.top_k_frequent_elements import f


class Test(unittest.TestCase):
    def setUp(self):
        self.f = f
    def test_1(self):
        self.assertListEqual(self.f([1,1,1,2,2,3], 2), [1,2])
    def test_2(self):
        self.assertListEqual(self.f([1], 1), [1])
    def test_3(self):
        self.assertListEqual(self.f([1.1,1.1,1.1,2,2,3], 2), [1.1,2])
