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
        if self.dummy.next == self.dummy:
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
            if item < cur.item:
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
            if item == cur.item:
                return idx
            idx += 1
        else:
            return None

    def pop(self, index):
        '''Removes and returns item at index (assuming head of list is index 0).
           If index is negative or >= size of list, raises IndexError
           MUST have O(n) average-case performance'''
        if index < 0 or index >= self.size():
            raise IndexError
        cur = self.dummy.next
        popped = self.dummy.next.item
        count = 0
        while count != index:
            popped = cur.next.item
            cur = cur.next
            count += 1
        cur.prev.next = cur.next
        cur.next.prev = cur.prev
        return popped

    def search(self, item):
        '''Searches OrderedList for item, returns True if item is in list, False otherwise"
           To practice recursion, this method must call a RECURSIVE method that
           will search the list
           MUST have O(n) average-case performance'''
        return self.helper_search(item, self.dummy.next)

    def helper_search(self, item, node):
        if node == self.dummy:
            return False
        elif node.item > item:
            return False
        elif node.item == item:
            return True
        else:
            node = node.next
            return self.helper_search(item, node)

    def python_list(self):
        '''Return a Python list representation of OrderedList, from head to tail
           For example, list with integers 1, 2, and 3 would return [1, 2, 3]
           MUST have O(n) performance'''
        lst = []
        cur = self.dummy
        while cur.next != self.dummy:
            cur = cur.next
            lst.append(cur.item)
        return lst

    def python_list_reversed(self):
        '''Return a Python list representation of OrderedList, from tail to head, using recursion
           For example, list with integers 1, 2, and 3 would return [3, 2, 1]
           To practice recursion, this method must call a RECURSIVE method that
           will return a reversed list
           MUST have O(n) performance'''
        return self.helper_python_list_reversed(self.dummy.prev)

    def helper_python_list_reversed(self, node):
        lst = [node.item]
        node = node.prev
        if node == self.dummy:
            return lst
        return lst + self.helper_python_list_reversed(node)


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

