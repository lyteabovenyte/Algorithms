'''
    Given a singly linkedlist and an integer m, for each integer k, if k appears more than m times
    in L, remove all nodes from L containing k.
'''
from ListNode import ListNode

def remove_if_appears_more_than_threshold(L, m):
    dummy_head = ListNode(0, L)
    current = dummy_head.next
    prev = dummy_head

    count = 0
    while current:
        if current.data == prev.data:
            current = current.next
            count += 1
        if current.data != prev.data and count < m:
            prev = current
            current = current.next
            count = 0
        if count >= m:
            # we should remove all the nodes, cause it violates the threshold.
            prev.next = current
            prev = current
            current = current.next
            count = 0

    return L