import unittest
from leetcode.permutation_in_string import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertTrue(self.f("ab", "eidbaooo"))

    def test_two(self):
        self.assertTrue(self.f("adc", "dcda"))

    def test_three(self):
        self.assertFalse(self.f("ab", "eidboaoo"))
