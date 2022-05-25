import unittest
import collections
from leetcode.group_anagrams import f


class Test(unittest.TestCase):
    def setUp(self):
        self.f = f
    @staticmethod
    def assertItemsEqual(l1, l2):
        assert len(l1) == len(l2)
        for sl1, sl2 in zip(l1, l2):
            sl1.sort()
            sl2.sort()
        for sl1 in l1:
            assert sl1 in l2
    def test_1(self):
        self.assertItemsEqual(self.f(["eat","tea","tan","ate","nat","bat"]), [["bat"],["nat","tan"],["ate","eat","tea"]])
    def test_2(self):
        self.assertItemsEqual(self.f(["",""]), [["",""]])
    def test_3(self):
        self.assertItemsEqual(self.f(["","b"]), [[""],["b"]])


if __name__ == "__main__":
    unittest.main()
