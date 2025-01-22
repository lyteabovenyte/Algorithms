'''
    Given a singly linkedlist, return null if there does not exist any
    cycle in the linkedlist, and return the node at the start of the cycle 
    if there does exist a cycle.
'''
from ListNode import ListNode, create_linked_list, print_linked_list

def cyclic_or_not(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # we detect a cycle, now we start finding out
            # the start of the cycle.
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # both iterators advance in tandem
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it
    return None

# To solve this problem, we can use Floyd’s Tortoise and Hare algorithm 
# (also called the cycle detection algorithm).
# This approach detects a cycle in a 
# linked list and also identifies the node where the cycle starts.

def detect_cycle(head):
    if not head or not head.next:
        return None

    # Step 1: Detect if there is a cycle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # Cycle detected
            break
    else:
        # No cycle
        return None

    # Step 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Start of the cycle