'''
    implementing a LinkedList class.

    it worth noting that linked-lists are created in the heap,
    and a reference to the head will be on the stack, so
    after deleting a node with just `node.next = node.next.next` 
    GC will clean the node and erase it from the heap.
'''

class ListNode:
    
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
        
    # impelementing the basic list API -search, insert, delete- for singly linkedlist
    def search_list(L, key):
        while L and L.data != key:
            L = L.next
        # if key was not found in the list, L will have become null
        return L
    
    def insert_after(node, new_node):
        # insert a new node after a specified node
        new_node.next = node.next
        node.next = new_node
            
    def delete_after(node):
        # delete the node past this one, Assume node is not a tail
        node.next = node.next.next

# Helper function to create a linked list from a list.
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to print a linked list.
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> " if current.next else "\n")
        current = current.next