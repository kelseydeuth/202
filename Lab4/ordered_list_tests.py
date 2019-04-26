#
#Kelsey Deuth
#
#04/25/19
#
#Lab4
#Section 11
#Test cases for a doubly linked list

import unittest
from ordered_list import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        self.assertTrue(t_list.is_empty())
        self.assertFalse(t_list.search(10))
        t_list.add(10)
        self.assertFalse(t_list.remove(11))
        self.assertEqual(t_list.pop(0), 10)
        t_list.add(10)
        t_list.add(12)
        t_list.add(13)
        self.assertEqual(t_list.python_list(), [10,12,13])
        self.assertEqual(t_list.python_list_reversed(), [13,12,10])
        self.assertEqual(t_list.index(12), 1)
        self.assertEqual(t_list.index(13), 2)
        self.assertTrue(t_list.search(13))
        self.assertFalse(t_list.search(11))
        self.assertEqual(t_list.index(14), None)
        with self.assertRaises(IndexError):
            self.assertEqual(t_list.pop(4))
        with self.assertRaises(IndexError):
            self.assertEqual(t_list.pop(-3))
        self.assertEqual(t_list.pop(2), 13)


if __name__ == '__main__':
   unittest.main()


