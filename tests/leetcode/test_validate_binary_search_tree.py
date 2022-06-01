import unittest
from leetcode.validate_binary_search_tree import f
from leetcode.lib.binary_tree import array_to_binary_tree


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        root = array_to_binary_tree([2,1,3])
        self.assertTrue(f(root))

    def test_two(self):
        root = array_to_binary_tree([5,1,4,None,None,3,6])
        self.assertFalse(f(root))
