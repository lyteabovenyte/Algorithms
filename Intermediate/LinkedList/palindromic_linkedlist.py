'''
    Given a singly linkedlist, examine whether it is palindromic or not.
'''
from ListNode import ListNode

def palindromic_list(L):
    def reverse(head):
        dummy = ListNode(0)
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

    fast = slow = L
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # here, slow is at the start of the second half
    first_half_iter, second_half_iter = L, reverse(slow)
    while first_half_iter and second_half_iter:
        if first_half_iter.data != second_half_iter.data:
            return False
        first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next

    return True 
