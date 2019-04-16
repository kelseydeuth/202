import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
# from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack4 = Stack(0)
        stack.push(0)
        stack1 = Stack(7)
        stack1.push(1)
        stack1.push(5)
        stack2 = Stack(1)
        stack2.push(1)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)
        self.assertTrue(stack4.is_empty())
        self.assertTrue(stack4.is_full())
        with self.assertRaises(IndexError):  #checks for exception
            stack2.push(1)
        with self.assertRaises(IndexError):  #checks for exception
            stack4.pop()
        with self.assertRaises(IndexError):  #checks for exception
            stack4.peek()
        stack.push(3)
        self.assertEqual(stack.size(), 2)


if __name__ == '__main__': 
    unittest.main()

