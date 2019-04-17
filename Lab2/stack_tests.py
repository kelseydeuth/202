import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):

    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(), 1)

    def test1(self):
        stack1 = Stack(1)
        stack1.push(2)
        self.assertFalse(stack1.is_empty())
        self.assertTrue(stack1.is_full())
        with self.assertRaises(IndexError):  #checks for exception
            stack1.push(1)

    def test2(self):
        stack2 = Stack(5)
        stack2.push(3)
        stacktest = Stack(0)
        self.assertEqual(stack2.pop(), 3)
        with self.assertRaises(IndexError):  #checks for exception
            stacktest.pop()
        with self.assertRaises(IndexError):  #checks for exception
            stacktest.peek()

    def test3(self):
        stack3 = Stack(3)
        stack3.push(7)
        stack3.push(6)
        stack3.push(5)
        stacktest = Stack(0)
        self.assertEqual(stack3.peek(), 5)
        #self.assertEqual(stack3.peek(), 6)
        #self.assertEqual(stack3.pop(), 5)
        #self.assertEqual(stack3.pop(), 6)
        #self.assertEqual(stack3.pop(), 7)
        self.assertEqual(stack3.size(), 3)
        self.assertFalse(stack3.is_empty())
        self.assertTrue(stacktest.is_empty())


if __name__ == '__main__': 
    unittest.main()

