import unittest
import lib


class TestLib(unittest.TestCase):
    def test_check1(self):
        myList = [[1, 3, 5], [3, 5, 7], [2, 5, 3]]
        self.assertEqual(lib.check_lists(myList), 2)

    def test_check2(self):
        myList = [[1, -5, 7], [2, 7, 14], [-6, 8, 7], [12, 7, -10]]
        self.assertEqual(lib.check_lists(myList), 1)

    def test_check3(self):
        myList = [[-57, 44, 66], [-90, 2, 17]]
        self.assertEqual(lib.check_lists(myList), 0)


if __name__ == '__main__':
    unittest.main()