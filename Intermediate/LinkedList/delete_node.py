'''
    Given a singly linkedlist, delete a node from the linkedlist.
'''

# Time complexity: O(n)
def delete_node(head, value):
    current = head
    prev = None
    while current.data != value:
        prev = current
        current = current.next
    
    prev.next = current.next
        

# Time complexity: O(1)
'''
    copy the data field of the next node
    on the wanted node, and point it's next
    to the next Node's next field
'''
def delete2(node):
    # node is the pointer to the one node we want to delete
    next_node = node.next
    node.data = next_node.data
    node.next = next_node.next

