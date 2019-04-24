#
#Kelsey Deuth
#
#04/18/19
#
#Lab2
#Section 11
#This code initializes a data structure and organizes data in a stacked array structure




class Stack:
    '''Implements an efficient last-in first-out Abstract Data Type using a Python List'''

    def __init__(self, capacity):
        '''Creates and empty stack with a capacity'''
        self.capacity = capacity
        self.items = [None] * capacity
        self.num_items = 0

"stack_array.py" 73L, 2161C

