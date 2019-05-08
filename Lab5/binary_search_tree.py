#
#Kelsey Deuth
#kdeuth@calpoly.edu
#05/07/19
#
#Lab5
#Section 11
#Creates a binary search tree
#

class TreeNode:
    def __init__(self, key, data, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

class BinarySearchTree:

    def __init__(self): # Returns empty BST
        self.root = None

    def is_empty(self): #returns True if tree is empty, else False
        if self.root is None:
            return True
        return False

    def search(self, key): # returns True if key is in a node of the tree, else False
        if self.is_empty():
            return False
        return search_help(self.root, key)

    def insert(self, key, data=None): # inserts new node w/ key and data
        # If an item with the given key is already in the BST, 
        # the data in the tree will be replaced with the new data
        # Example creation of node: temp = TreeNode(key, data)
        new = TreeNode(key, data)
        if self.is_empty() is True:
            self.root = new
            return
        node = self.root
        while True:
            if key > node.key:
                if node.right is None:
                    node.right = new
                    break
                else:
                    node = node.right
            elif key < node.key:
                if node.left is None:
                    node.left = new
                    break
                else:
                    node = node.left
            elif key == node.key:
                node.data = data
                break

    def find_min(self): # returns a tuple with min key and data in the BST
        # returns None if the tree is empty
        if self.is_empty() is True:
            return None
        node = self.root
        while True:
            if node.left is None:
                return node.key, node.data
            else:
                node = node.left

    def find_max(self): # returns a tuple with max key and data in the BST
        # returns None if the tree is empty
        if self.is_empty() is True:
            return None
        node = self.root
        while True:
            if node.right is None:
                return node.key, node.data
            else:
                node = node.right

    def tree_height(self): # return the height of the tree
        # returns None if tree is empty
        if self.is_empty() is True:
            return None
        return height_help(self.root)

    def inorder_list(self): # return Python list of BST keys representing in-order traversal of BST
        return inorder_help(self.root)

    def preorder_list(self):  # return Python list of BST keys representing pre-order traversal of BST
        return preorder_help(self.root)
        
    def delete(self, key): # deletes node containing key
        # Will need to consider all cases 
        # This is the most difficult method - save it for last, so that
        # if you cannot get it to work, you can still get credit for 
        # the other methods
        # Returns True if the item was deleted, False otherwise
        pass


def search_help(n, key):
    if n is None:
        return False
    if n.key == key:
        return True
    if search_help(n.left, key):
        return True
    if search_help(n.right, key):
        return True
    return False


def height_help(n):
    if n.left is None and n.right is None:
        return 0
    if n.left is None:
        return 1 + height_help(n.right)
    if n.right is None:
        return 1 + height_help(n.left)
    return 1 + max(height_help(n.left), height_help(n.right))


def inorder_help(n):
    if n is None:
        return []
    return inorder_help(n.left) + [n.key] + inorder_help(n.right)


def preorder_help(n):
    if n is None:
        return []
    return [n.key] + preorder_help(n.left) + preorder_help(n.right)
