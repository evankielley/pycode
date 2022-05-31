import unittest
from leetcode.three_sum import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f

    def test_one(self):
        actuals = f([-1,0,1,2,-1,-4])
        expecteds = [[-1,-1,2],[-1,0,1]]
        assert len(actuals) == len(expecteds)
        for actual, expected in zip(*[actuals, expecteds]):
            self.assertListEqual(actual, expected)

    def test_two(self):
        actuals = f([])
        expecteds = []
        assert len(actuals) == len(expecteds)
        for actual, expected in zip(*[actuals, expecteds]):
            self.assertListEqual(actual, expected)

    def test_three(self):
        actuals = f([0])
        expecteds = []
        assert len(actuals) == len(expecteds)
        for actual, expected in zip(*[actuals, expecteds]):
            self.assertListEqual(actual, expected)

    def test_four(self):
        actuals = f([0,0,0,0])
        expecteds = [[0,0,0]]
        assert len(actuals) == len(expecteds)
        for actual, expected in zip(*[actuals, expecteds]):
            self.assertListEqual(actual, expected)
