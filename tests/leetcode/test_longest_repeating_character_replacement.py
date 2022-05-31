import unittest
from leetcode.longest_repeating_character_replacement import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertEqual(self.f("ABAB", 2), 4)

    def test_two(self):
        self.assertEqual(self.f("AABABBA", 1), 4)
