import unittest
from leetcode.insert_interval import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        expected = [[1, 5], [6, 9]]
        actual = self.f([[1,3],[6,9]], [2,5])
        for l1, l2 in zip(*[expected, actual]):
            self.assertListEqual(l1, l2)
    
    def test_two(self):
        expected = [[3, 5], [6, 6], [12, 15]]
        actual = self.f([[3,5],[12,15]], [6,6])
        for l1, l2 in zip(*[expected, actual]):
            self.assertListEqual(l1, l2)
