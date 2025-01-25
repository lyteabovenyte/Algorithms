'''
    Given a linkedlist and an integer x, return a list in such a way that all nodes which data
    less than x appears first, then the nodes with data equal to x, then the nodes with data greater
    than x, the relative ordering of each group should be maintained.
'''
from typing import Optional
from ListNode import ListNode

def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    less_head = less_iter = ListNode()
    equal_head = equal_iter = ListNode()
    greater_head = greater_iter = ListNode()

    while l:
        if l.data < x:
            less_iter.next = l
            less_iter = less_iter.next
        elif l.data == x:
            equal_iter.next = l
            equal_iter = equal_iter.next
        else:
            greater_iter.next = l
            greater_iter = greater_iter.next
        l = l.next
    
    # combine these three
    greater_iter.next = None
    equal_iter.next = greater_head.next
    less_iter.next = equal_head.next
    return less_head.next