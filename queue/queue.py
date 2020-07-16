"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
"""
Assumptions:
- Lists are inherent in Python
- Can use built in functionality to achieve results
- LinkedLists linear approach to counting easier when counting while adding
"""

# Array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         # must update the size when checking
#         self.size = len(self.storage)
#         return self.size

#     def enqueue(self, value):
#         self.storage.insert(0, value)

#     def dequeue(self):
#         # first check if there are any items in the list
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop()

import sys
sys.path.append(".")

from singly_linked_list.singly_linked_list import LinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Store Data through invocation of the LinkedList
        self.storage = LinkedList()

    def __len__(self):
        # Returning the tracked size of the Linked list
        return self.size
        
    def enqueue(self, value):
        # Add to size as adding items
        self.size += 1
        # add item to the tail through LinkedList methods
        self.storage.add_to_tail(value)
            
    def dequeue(self):
        # Establish empty size of List
        if self.storage.head == None:
            self.size = 0
        else:
            # Subtract as removing items
            self.size -= 1
            return self.storage.remove_head()