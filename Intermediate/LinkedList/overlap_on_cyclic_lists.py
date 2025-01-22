'''
    Given two singly linkedlist which may have cycles, find the overlap
    between these two.
'''
from cyclic_or_not import cyclic_or_not
from overlapping_lists import overlapping_no_cycle_lists

def overlap_with_cycle(L1, L2):
    # stores the start of cycle if any
    root1, root2 = cyclic_or_not(L1), cyclic_or_not(L2)

    if not root1 and not root2:
        return overlapping_no_cycle_lists(L1, L2)
    
    if (not root1 and root2) or (not root2 and root1):
        return None
    
    # so both lists have cycles
    temp = root2
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break

    # L1 and L2 do not end in the same cycle.
    if temp is not root1:
        return None  # cycles are disjoint
    
    # Helper function to calculate the distance between a and b
    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis
    
    stem1_len, stem2_len = distance(L1, root1), distance(L2, root2)
    if stem1_len > stem2_len:
        L1, L2 = L2, L1
        root1, root2 = root2, root1

    for _ in range(abs(stem1_len - stem2_len)):
        L2 = L2.next

    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1, L2 = L1.next, L2.next

    return L1 if L1 is L2 else root1 # or root2 -doesn't make any difference

