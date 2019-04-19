#
#Kelsey Deuth
#
#04/18/19
#
#Lab3
#Section 11
#this code uses an array data structure to create a queue
#


class Queue:
    '''Implements an array-based, efficient first-in first-out Abstract Data Type
       using a Python array (faked using a List)'''

    def __init__(self, capacity):
        '''Creates an empty Queue with a capacity'''
        self.items = [None] * capacity
        self.capacity = capacity
        self.num_items = 0
        self.front = 0
        self.end = 0

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
        '''If Queue is not full, enqueues (adds) item to Queue 
           If Queue is full when enqueue is attempted, raises IndexError'''
        if self.num_items == self.capacity:
            raise IndexError
        else:
            self.items[self.end] = item
            self.end = (self.end+1) % self.capacity
            self.num_items += 1

    def dequeue(self):
        '''If Queue is not empty, dequeues (removes) item from Queue and returns item.
           If Queue is empty when dequeue is attempted, raises IndexError'''
        if self.num_items == 0:
            raise IndexError
        else:
            n = self.items[self.front]
            self.front = (self.front + 1) % self.capacity
            self.num_items -= 1
            return n

    def size(self):
        '''Returns the number of elements currently in the Queue, not the capacity'''
        return self.num_items


