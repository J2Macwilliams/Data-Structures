"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

"""
Assumptions:
- Lists are inherent in Python
- Can use built in functionality to achieve results
- Must account for items as they are added and removed from Linked Lists
"""


# Array
# class Stack:
#     def __init__(self):
#         self.size = 0
#         # With list stack must start with an empty list
#         self.storage = []
        
#     def __len__(self):
#         # must update the size when checking
#         self.size = len(self.storage)
#         return self.size

#     def push(self, value):
#         # must append new value to the list
#         self.storage.append(value)

#     def pop(self):
#         # first check if there are any items in the list
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop()
import sys
sys.path.append(".")

from singly_linked_list.singly_linked_list import LinkedList 


# Linked List
class Stack:
    def __init__(self):
        self.size = 0
        # Store Data through invocation of the LinkedList
        self.storage = LinkedList()

    def __len__(self):
        # Returning the tracked size of the Linked list
        return self.size

    def push(self, value):
        # Add to size as adding items
        self.size += 1
        # add item to the tail through LinkedList methods
        return self.storage.add_to_tail(value)

    def pop(self):
        # Establish empty size of List
        if self.storage.head == None:
            self.size = 0
        else:
            # Subtract as removing items
            self.size -= 1
            return self.storage.remove_tail()
