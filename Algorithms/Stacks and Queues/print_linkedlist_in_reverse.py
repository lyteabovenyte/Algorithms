'''
    This program uses stacks to return a singly linkedlist in reverse order.
'''

def print_linked_lsit_in_reverse(head):
    nodes = []
    
    while head:
        nodes.append(head.data)
        head = head.next 
        
    while nodes:
        print(nodes.pop())