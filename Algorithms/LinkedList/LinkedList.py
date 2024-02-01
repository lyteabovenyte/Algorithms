class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    
    def is_empty(self):
        return self.head is None
    
    def insert_first(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        
    def insert_after(self, perd_value, value):
        '''
            takes two arguments: the value of the node after which the new node 
            should be inserted, and the value of the new node.
        '''
        pred = self.head
        while pred is not None and pred.data != perd_value:
            pred = pred.next
            
        if pred is not None:
            # The predecessor node is found
            node = Node(value)
            node.next = pred.next
            pred.next = node
            
    
    def insert_last(self, value):
        if self.is_empty():
            self.head = Node(value)
            return
        pred = self.head
        while pred.next is not None:
            pred = pred.next
        pred.next = Node(value)
        
        
    def delete_last(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            ## If there's only one element in list 
            temp = self.head
            self.head = None
            return temp
        pred = self.head
        temp = self.head.next
        while temp.next is not None:
            pred = pred.next
            temp = temp.next 
        pred.next = None
        return temp
    
    
    def delete_by_value(self, value):
        '''
            "Deletion in the middle" refers to the general concept of removing
            and element somewhere within a linkedlist, not from the beginning or the end.
        '''
        if self.is_empty():
            return None
        
        if self.head.data == value:
            temp = self.head
            self.head = self.head.next
            return temp
        
        pred = self.head
        temp = self.head.next
        
        while temp is not None and temp.data != value:
            pred = pred.next
            temp = temp.next 
            
        if temp is not None:
            # Found it!
            pred.next = temp.next 
        return temp  #return deleted object can be useful if we want to continue to use it outside the list.
    
    
    def delete_first(self):
        if self.is_empty():
            return None
        temp = self.head
        self.head = self.head.next
        return temp
    
    