'''
    Given a singly linkedlist and an integer k, remove the kth last element from the linkedlist.
    Assume linkedlist has at least k nodes, delete the k-th last node in L.
'''
from ListNode import ListNode

# idea: moving forward in tandem.
def remove_kth_last_element(head, k):

    dummy_head = ListNode(0, head)
    first = dummy_head.next
    for _ in range(k):
        first = first.next

    second = dummy_head.next
    while first:
        first, second = first.next, second.next

    # now, second points to the (k + 1)-th last node, delete it's successor.
    second.next = second.next.next
    return dummy_head.next

