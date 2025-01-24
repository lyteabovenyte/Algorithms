'''
    Given a singly linkedlist, implement the even odd merge, which first comes the even numbered node
    then the odd numbered ones
'''
from ListNode import ListNode

def even_odd_merge(L):
    if not L:
        return L

    even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
    tails, turn = [even_dummy_head, odd_dummy_head], 0
    while L:
        tails[turn].next = L
        L = L.next
        tails[turn] = tails[turn].next
        # turn is the indicator to determine which group we are appending.
        turn ^= 1
    tails[1].next = None
    tails[0].next = odd_dummy_head.next
    return even_dummy_head.next