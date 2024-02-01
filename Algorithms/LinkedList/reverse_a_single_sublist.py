from ListNode import ListNode
from LinkedList import Node


def reverse_sublist(head, start, end):
    """
    Reverse a sub-list of the linked list.
    write a program which takes a singly linked list L and two integers , start and finish as arguments,
    and reverse the order of the nodes from the startth node to finishth node , inclusive.
    the numbering begin with 1.
    """
    
    #Find the node before and after the sublist
    before = head
    for _ in range(start - 1):
        before = before.next 
    after = end.next 
    
    current = start
    while current != end:
        nxt = current.next
        current.next = before
        before = current
        current = nxt
        
    #Connect the sublist to the rest of the list
    before.next = after 
    
    return head

