import unittest
from leetcode.longest_substring_without_repeating_characters import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertEqual(f(""), 0)

    def test_two(self):
        self.assertEqual(f("a"), 1)

    def test_three(self):
        self.assertEqual(f("abcabcbb"), 3)

    def test_four(self):
        self.assertEqual(f("bbbbb"), 1)

    def test_five(self):
        self.assertEqual(f("pwwkew"), 3)
