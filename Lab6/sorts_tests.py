#
#Kelsey Deuth
#kdeuth@calpoly.edu
#05/15/19
#
#Lab6
#Section 11
#Tests code from the sort.py file
#
import unittest
from sorts import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

        nums = [23, 10]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection_sort(self):
        nums = [3, 5, 6, 9, 2, 1, 4, 8]
        c = selection_sort(nums)
        self.assertEqual(c, 28)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 8, 9])

    def test_selection_sort_e(self):
        nums = []
        c = selection_sort(nums)
        self.assertEqual(c, 0)
        self.assertEqual(nums, [])

    def insertion_sort(self):
        nums = [3, 5, 6, 9, 2, 1, 4, 8]
        c = insertion_sort(nums)
        self.assertEqual(c, 28)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 8, 9])

    def test_insertion_sort_e(self):
        nums = []
        c = insertion_sort(nums)
        self.assertEqual(c, 0)
        self.assertEqual(nums, [])


if __name__ == '__main__': 
    unittest.main()

