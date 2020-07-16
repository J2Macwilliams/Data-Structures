"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

from queue import Queue
from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert here
            if self.left is None:
                self.left = BSTNode(value)
            else: 
                # repeat the process on left subtree
                self.left.insert(value)
        # Case 2: value is greater than or equal the self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # case 2: if target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()
                
            

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # base case
        if self is None:
            return 
        # apply function to self
        else:
            fn(self.value)
            # recursive for left and right nodes
            if self.left is not None:
                self.left.for_each(fn)
            if self.right is not None:
                self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current Node is None
        # reached the end of the recursion
        if self is None:
            return self
            
        # check if we can move left
        if self.left is not None:
            self.left.in_order_print(node)

        # visit the node and print it's value
        print(self.value)

        # check if we can move right
        if self.right is not None:
            self.right.in_order_print(node)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # establish a queue from the imported class
        my_queue = Queue()
        # place the root in the queue
        my_queue.enqueue(node)

        # establish a while loop
        # checking for the size of the queue
        while my_queue.size > 0:
            # dequeue bottom item
            current = my_queue.dequeue()
            # print the item
            print(current.value)

            # place current items left node in queue if not None
            if current.left is not None:
                my_queue.enqueue(current.left)
            # place current items right node in queue if not None
            if current.right is not None:
                my_queue.enqueue(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize and empty stack
        my_stack = Stack()
        # push the root node onto the stack
        my_stack.push(node)

        # create a while loop to manage iteration
        while my_stack.size > 0:
            # pop item off the stack
            current = my_stack.pop()
            # print the current item
            print(current.value)

            # if there is a right subtree
            if current.right is not None:
                # push item onto the stack
                my_stack.push(current.right)

            # if there is a left subtree
            if current.left is not None:
                # push item onto the stack
                my_stack.push(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # visit root node
        if self is None:
            return
        print(self.value)
        if self.left is not None:
            self.left.pre_order_dft(node)
        if self.right is not None:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # if the current Node is None
        # reached the end of the recursion
        if self is None:
            return self

        # check if we can move left
        if self.left is not None:
            self.left.post_order_dft(node)

        # check if we can move right
        if self.right is not None:
            self.right.post_order_dft(node)

        # visit the node and print it's value
        print(self.value)

            
        