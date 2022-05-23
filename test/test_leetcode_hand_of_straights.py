import unittest
from leetcode.hand_of_straights import f


class Test(unittest.TestCase):

    def setUp(self):
        self.f = f
    def test_1(self):
        self.assertEqual(self.f([1,2,3,6,2,3,4,7,8], 3), True)
    def test_2(self):
        self.assertEqual(self.f([8,8,9,7,7,7,6,7,10,6], 2), True)


if __name__ == "__main__":
    unittest.main()
