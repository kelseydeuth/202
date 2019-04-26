#
#Kelsey Deuth
#
#04/25/19
#
#Lab4
#Section 11
#Creates a doubly linked list



class Node:
    '''Node for use with doubly-linked list'''
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class OrderedList:
    '''A doubly-linked ordered list of items, from lowest (head of list) to highest (tail of list)'''

    def __init__(self):
        '''Use ONE dummy node as described in class
           ***No other attributes***
           Do not have an attribute to keep track of size'''
        self.dummy = Node(None)
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy

    def is_empty(self):
        '''Returns back True if OrderedList is empty
            MUST have O(1) performance'''
        if self.dummy.next is None:
            return True
        return False

    def add(self, item):
        '''Adds an item to OrderedList, in the proper location based on ordering of items
           from lowest (at head of list) to highest (at tail of list)
           If the item is already in the list, do not add it again 
           MUST have O(n) average-case performance'''
        n = Node(item)
        cur = self.dummy
        while cur.next != self.dummy.next:
            cur = cur.next
            if item < cur.data:
                break
        cur.prev.next = n
        n.next = cur
        n.prev = cur.prev
        cur.prev = n

    def remove(self, item):
        '''Removes an item from OrderedList. If item is removed (was in the list) returns True
           If item was not removed (was not in the list) returns False
           MUST have O(n) average-case performance'''
        cur = self.dummy
        while cur.next != self.dummy:
            cur = cur.next
            if item == cur.item:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return True
            else:
                return False


    def index(self, item):
        '''Returns index of an item in OrderedList (assuming head of list is index 0).
           If item is not in list, return None
           MUST have O(n) average-case performance'''
        idx = 0
        cur = self.dummy
        while cur.next != self.dummy:
            cur = cur.next
            idx += 1
            if item == cur.item:
                return idx - 1
            return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index > self.size():
            raise IndexError
        else:
            idx = 0
            cur = self.dummy
            while idx != index:
                cur = cur.next
                idx += 1
            return cur.prev.item
        cur = cur.prev
        cur.prev.next = cur.next
        cur.next.prev = cur.prev


    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        cur = self.dummy
        if item == cur.item:
            return True
        if cur.next == self.dummy:
            return False
        return self.search(cur.next)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        lst = []
        cur = self.dummy
        while cur.next != self.dummy:
            cur = cur.next
            lst.append(cur.item)
        return lst[::-1]

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        lst = []
        cur = self.dummy
        while cur.next != self.dummy:
            cur = cur.next
            lst.append(cur.item)
        return lst[::-1]

    def size(self):
        '''Returns number of items in the OrderedList
           To practice recursion, this method must call a RECURSIVE method that
           will count and return the number of items in the list
           MUST have O(n) performance'''
        return self.size_helper(self.dummy.next)

    def size_helper(self, node):
        if node == self.dummy:
            return 0
        return self.size_helper(node.next) + 1

