'''
    Given two sorted linked lists, merge them in a way which the result linkedlist 
    is also sorted.
    the only field you can change in a linked list is it's next field.
'''
from ListNode import ListNode
from typing import Optional

def merge_two_sorted_list(L1: Optional[ListNode],
                          L2: Optional[ListNode]) -> Optional[ListNode]:
    
    # creating a placeholder for the result
    dummy_head = tail = ListNode()

    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        
        tail = tail.next
    
    # Append the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head.next


def merge_doubly_linked_list(L1: Optional[ListNode],
                             L2: Optional[ListNode]):
    
    dummy_head = tail = ListNode()
    tail.prev, tail.next = None, None

    while L1 and L2:
        if L1.data < L2.data:
            tail, L1 = L1, L1.next
        else:
            tail, L2 = L2, L2.next

        tail = tail.next
        tail.prev


