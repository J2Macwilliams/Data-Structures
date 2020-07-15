"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
    
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if self.head is None:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = new_node
        # if DLL is not empty
        else:
            # set new node's next to current head
            new_node.next = self.head
            new_node.prev = None
            # set head's prev to new node
            self.head.prev = new_node
            # set head to the new node
            self.head = new_node

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        # store the value of the head
        saved = self.head
        # decrement the length of the DLL
        self.length -= 1
        # delete the head
        if self.head is None:
            return
        # if head.next is not None
        if self.head.next is not None:
            # set head.next's prev to None
            self.head.next.prev = None
            # set head to head.next
            self.head = self.head.next
            # else (if head.next is None)
        elif self.head.next is None:
            # set head and tail to None
            self.head = None
            self.tail = None
        # return the value
        return saved

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value):
        # create instance of ListNode with value
        new_node = ListNode(value)
        # increment the DLL length attribute
        self.length += 1
        # if DLL is empty
        if not self.head and not self.tail:
            # set head and tail to the new node instance
            self.head = new_node
            self.tail = self.head
        # if DLL is not empty
        else:
            # set new node's prev to current tail
            new_node.prev = self.tail
            # set tail's next to new node
            self.tail.next = new_node
            # set tail to the new node
            self.tail = new_node

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        # store the value of the tail
        saved = self.tail
        # decrement the length of the DLL
        self.length -= 1
        # delete the tail
        # if tail.prev is not None
        if self.tail is None:
            return
        elif self.tail.prev is not None:
            # assign pointers to previous
            self.tail.prev.next = None
            # assign new tail
            self.tail = self.tail.prev
        # else (if tail.prev is None)
        elif self.tail.prev is None:
            # set head and tail to None
            self.head = None
            self.tail = None
        return saved

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        # Create variable for current
        current = self.head
        # check for match to node
        if self.head is node:
            return
        # traverse if not
        else:
            current = current.next
            if current is node:
                # when found change pointers
                # previous position pointers
                current.prev = None
                current.next = self.head
                # add to head pointers
                self.head.prev = current
                self.head.next = current.next
                # set changed node to current
                self.head = current

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        # base case
        if self.head is None or node is None:
            return
        # check if node is tail
        elif node is self.tail:
            return
        # check if head is node
        elif node is self.head:
            # create var for head
            temp = self.head.next
            # assing new head prev pointer
            temp.prev = None
            # assign head to tail position
            self.head.prev = self.tail
            self.head.net = None
            # change tail's pointers
            self.tail.next = self.head
            # change head and tail
            self.tail = self.head
            self.head = temp
        else:
            current = self.head.next
            if current is node:
                # assign surrounding pointers to each other
                current.prev.next = current.next
                current.next.prev = current.prev
                # assing current to tail
                current.prev = self.tail
                current.next = None
                # change tails pointer
                self.tail.next = current
                # assign new tail
                self.tail = current
        
        

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # $%$Start
        self.length -= 1
        if not self.head and not self.tail:
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head == node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        # $%$End
            
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value 


