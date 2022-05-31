import unittest
from leetcode.task_scheduler import f


class Test(unittest.TestCase):
    def setUp(self):
        self.f = f
    def test_1(self):
        self.assertEqual(self.f(["A","A","A","B","B","B"], 2), 8)
    def test_2(self):
        self.assertEqual(self.f(["A","A","A","B","B","B"], 0), 6)
    def test_3(self):
        self.assertEqual(self.f(["A","A","A","A","A","A","B","C","D","E","F","G"], 2), 16)
