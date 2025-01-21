'''
    Write a program that takes a linkedlist and two integer s and f,
    and reverse the sublist of linkedlist from sth to fth element(inclusive).
    do not allocate additional space.
'''
from LinkedList import ListNode

def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0, L)

    for _ in range(1, start):
        # the previous node of the start_sublist_node
        sublist_head = sublist_head.next  

    # Reverse logic
    sublist_iter = sublist_head.next
    for _ in range(finish - start):
        temp = sublist_iter.next
        temp.next, sublist_iter.next, sublist_head.next = (sublist_head.next,
                                                           temp.next,
                                                           temp)
    # returning the original Linked_list's head.
    return dummy_head.next