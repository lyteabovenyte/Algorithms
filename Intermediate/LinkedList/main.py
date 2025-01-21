'''
    the original linked list class.
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __repr__(self):
        return self.data
    

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next
                
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return "-> ".join(nodes)
    
    # Traversing a linked-list
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # inserting into the beginning of the linkedlist
    def add_head(self, node):
        node.next = self.head
        self.head = node

    # inserting into the tail
    def add_tail(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass # goes up until the last node. and current_node become the tail.
        current_node.next = node

    # inserting after a specific node
    def insert_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("LinkedList is empty.")
        
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
            
        raise Exception(f'{target_node_data} not found!')
    
    # insert before a specific node
    def insert_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("LinkedList is empty")
        
        if self.head.data == target_node_data:
            self.add_head(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        
        raise Exception(f'{target_node_data} not found!')
    
    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("LinkedList is empty!")
        
        if self.head.data == target_node_data:
            self.head = self.head.next

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        
        raise Exception(f'{target_node_data} not found!')

    def get(self, position=None):
        if position == None:
            return self.head
        i = 0
        for node in self:
            if i == position:
                return node.data
            i += 1
        raise Exception(f'index out of range: index{position}')
    
    def reverse(self):
        # Two pointer approach
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self
    
    def reverse_segment(start, end):
        prev, current = None, start
        while current != end:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    # creating a queue from linkedlist
    def queue(self):
        from collections import deque
        q = deque()
        for ele in self:
            q.append(ele)
        return q
    

'''
    Circular linked lists are a type of linked list in which the last node 
    points back to the head of the list instead of pointing to None.
    Usage:
    - Going around each player's turn in a multiplayer game
    - Managing the application life cycle of a given operating system
    - Implementing a Fibonacci heap
'''
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None and node.next != self.head:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            node.append(str(node))
        return "-> ".join(nodes)

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))
    
