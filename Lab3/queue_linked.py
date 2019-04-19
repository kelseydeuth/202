#
#Kelsey Deuth
#
#04/18/19
#
#Lab3
#Section 11
#This code runs uses a linked list data structure to create a queue
#

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Queue:
    '''Implements an link-based ,efficient first-in first-out Abstract Data Type'''

    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.num_items = 0
        self.capacity = capacity

    def is_empty(self):
        '''Returns True if the Queue is empty, and False otherwise'''
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        '''Returns True if the Queue is full, and False otherwise'''
        if self.num_items == self.capacity:
            return True
        return False

    def enqueue(self, item):
        if self.is_full() is True:
            raise IndexError
        if self.num_items == 0:
            self.head = Node(item)
            self.tail = self.head
            self.num_items += 1
        else:
            newN = Node(item)
            self.tail.next = newN
            self.tail = newN
            self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.num_items == 0:
            raise IndexError
        else:
            n = self.head.item
            self.head = self.head.next
            self.num_items -= 1
            return n

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items

