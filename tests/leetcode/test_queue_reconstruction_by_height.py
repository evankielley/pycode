import unittest
from leetcode.queue_reconstruction_by_height import f


class Test(unittest.TestCase):
    def setUp(self):
        self.f = f
    def test_one(self):
        expected = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        actual = self.f([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])
        for l1, l2 in zip(*[expected, actual]):
            self.assertListEqual(l1, l2)
