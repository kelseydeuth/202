#
#Kelsey Deuth
#kdeuth@calpoly.edu
#05/07/19
#
#Lab5
#Section 11
#Tests for a binary search tree
#


import unittest
from binary_search_tree import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.is_empty())
        self.assertEqual(bst.search(10), False)
        bst.insert(10, 'stuff')
        self.assertTrue(bst.search(10))
        self.assertEqual(bst.find_min(), (10, 'stuff'))
        bst.insert(10, 'other')
        self.assertEqual(bst.find_max(), (10, 'other'))
        self.assertEqual(bst.tree_height(), 0)
        self.assertEqual(bst.inorder_list(), [10])
        self.assertEqual(bst.preorder_list(), [10])
        self.assertTrue(bst.delete(10))


    def test_2(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.delete(5))
        self.assertEqual(bst.tree_height(), None)
        self.assertEqual(bst.find_min(), None)
        self.assertEqual(bst.find_max(), None)
        bst.insert(10, 'stuff')
        bst.insert(12, 'more stuff')
        self.assertEqual(bst.tree_height(), 1)
        self.assertEqual(bst.find_max(), (12, 'more stuff'))
        bst.insert(9, 'even more stuff')
        self.assertEqual(bst.tree_height(), 1)
        bst.insert(9, 'new stuff')
        bst.insert(13, 'stuff again')
        self.assertEqual(bst.tree_height(), 2)
        self.assertEqual(bst.find_min(), (9, 'new stuff'))
        self.assertEqual(bst.find_max(), (13, 'stuff again'))
        self.assertTrue(bst.search(13))
        self.assertTrue(bst.search(9))
        self.assertTrue(bst.search(12))
        self.assertFalse(bst.search(15))
        self.assertFalse(bst.search(8))
        bst.insert(4, 'hehe stuff')
        self.assertEqual(bst.tree_height(), 2)
        self.assertTrue(bst.delete(4))
        self.assertTrue(bst.delete(13))
        self.assertFalse(bst.delete(11))
        self.assertFalse(bst.delete(5))
        self.assertFalse(bst.delete(15))
        self.assertTrue(bst.delete(9))
        self.assertTrue(bst.delete(10))

    def test_3(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.delete(5))
        bst.insert(10, 'stuff')
        self.assertTrue(bst.delete(10))
        bst.insert(10, 'stuff')
        bst.insert(9, 'stuff')
        bst.insert(12, 'stuff')
        self.assertTrue(bst.delete(12))
        self.assertTrue(bst.delete(9))
        bst.insert(9, 'stuff')
        self.assertTrue(bst.delete(10))
        bst.insert(12, 'stuff')
        bst.insert(14, 'stuff')
        self.assertTrue(bst.delete(9))
        bst.insert(4, 'stuff')
        bst.insert(5, 'stuff')
        self.assertTrue(bst.delete(12))
        self.assertTrue(bst.delete(4))














if __name__ == '__main__': 
    unittest.main()

