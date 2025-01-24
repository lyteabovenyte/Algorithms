'''
    Given a sorted linkedlist, remove duplicates from the linkedlist.
'''
from ListNode import ListNode

def remove_duplicates(head):
    dummy_head = ListNode(0, head)
    current = dummy_head.next
    prev = dummy_head

    while current:
        if prev.data == current.data:
            current = current.next
        else:
            prev.next = current
            prev = current
            current = current.next


# more undrestandable.
def remove_dup(L):
    it = L
    while it:
        # uses next_distinct to find the next_distinct value.
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L