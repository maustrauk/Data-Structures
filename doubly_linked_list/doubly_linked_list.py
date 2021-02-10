"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
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
        new_node = ListNode(value)
        old_head = self.head
        new_node.next = old_head

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return 

        old_head.prev = new_node
        self.head = new_node
        self.length += 1

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length == 0:
            return None

        value = self.head.value

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return value

        new_head = self.head.next
        self.head = new_head
        self.head.prev = None
        self.length -= 1

        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length = 1
            return

        

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return

        value = self.tail.value

        if self.length == 1:
            self.length = 0
            self.head = None
            self.tail = None
            
            return value

        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1

        return value


            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return
        
        if self.head is node:
            return

        if self.tail is node:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            self.add_to_head(node.value)
            return


        node.prev.next = node.next
        node.next.prev = node.prev

        self.length -= 1
        self.add_to_head(node.value)

        
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            return
        
        if self.tail is node:
            return

        if self.head is node:
            self.head = self.head.next
            self.head.prev = None
            self.length -= 1
            self.add_to_tail(node.value)
            return
            

        node.prev.next = node.next
        node.next.prev = node.prev

        self.length -= 1
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return
        
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        self.length -= 1

        if node.prev is None:
            self.head = self.head.next
            self.head.prev = None
            return
        
        if node.next is None:
            self.tail = self.tail.prev
            self.tail.next = None
            return

        node.prev.next = node.next
        node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max_value = self.head.value

        pointer = self.head

        while pointer is not None :
            if max_value < pointer.value:
                max_value = pointer.value
            
            pointer = pointer.next

        return max_value        
