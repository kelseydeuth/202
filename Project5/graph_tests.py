import unittest
from graph import *

class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        
    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    # queue tests!
    def test_queue(self):
        '''Trivial test to ensure method names and parameters are correct'''
        q = Queue(5)
        q.is_empty()
        q.is_full()
        q.enqueue('thing')
        q.dequeue()
        q.size()

    def test_simple(self):
        q = Queue(5)
        q.enqueue(0)
        self.assertFalse(q.is_empty())
        self.assertFalse(q.is_full())
        self.assertEqual(q.size(), 1)

    def test1(self):
        q1 = Queue(1)
        q1.enqueue(2)
        self.assertFalse(q1.is_empty())
        self.assertTrue(q1.is_full())

    def test2(self):
        q2 = Queue(5)
        q2.enqueue(3)
        qtest = Queue(0)
        self.assertEqual(q2.dequeue(), 3)
        with self.assertRaises(IndexError):  # checks for exception
            qtest.dequeue()

    def test3(self):
        b = Queue(3)
        b.enqueue('does')
        self.assertFalse(b.is_empty())
        b.enqueue('this')
        b.enqueue('work')
        self.assertTrue(b.is_full())
        with self.assertRaises(IndexError):
            b.enqueue('maybe')
        h = Queue(0)
        with self.assertRaises(IndexError):
            h.dequeue()

    # stack tests!
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
        self.assertEqual(stack3.size(), 3)
        self.assertFalse(stack3.is_empty())
        self.assertTrue(stacktest.is_empty())
        #stackNone = Stack(None)
        #with self.assertRaises(IndexError):  #checks for None exception
        #    stackNone.pop()

if __name__ == '__main__':
   unittest.main()
