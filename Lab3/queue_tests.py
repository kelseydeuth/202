#
#Kelsey Deuth
#
#04/18/19
#
#Lab3
#Section 11
#This code runs full test coverage on queue_array and queue_linked python files
#

import unittest
#from queue_array import Queue
from queue_linked import Queue

class TestLab1(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()

