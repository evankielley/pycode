import unittest
from leetcode.daily_temperatures import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        self.assertListEqual(f([73,74,75,71,69,72,76,73]), [1,1,4,2,1,1,0,0])

    def test_two(self):
        self.assertListEqual(f([30,40,50,60]), [1,1,1,0])

    def test_three(self):
        self.assertListEqual(f([30,60,90]), [1,1,0])
