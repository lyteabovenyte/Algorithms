'''
    Given a singly linkedlist and a nonnegative integer k, and returns the cyclically shifted
    to the right by k.
    Assume k < n --> the opposite side of this assumption, is right shift by n % k.
'''
from ListNode import ListNode

def cyclically_right_shift(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head
    res_head = ListNode(0, None)
    
    while k:
        k -= 1
        first = first.next
        
    res_head.next = first

    while first.next:
        first = first.next
    
    # first is tail now, so the next should be the head of the original L
    first.next = L

    return res_head

# another approach
def cyclically_right_shift1(L, k):
    if not L:
        return L
    
    tail, n = L, 1
    while tail.next:
        n += 1
        tail = tail.next

    tail.next = L

    new_tail, step_to_new_tail = tail, (n - k)
    while step_to_new_tail:
        new_tail = new_tail.next
        step_to_new_tail -= 1

    new_head = new_tail.next
    new_tail.next = None

    return new_head

