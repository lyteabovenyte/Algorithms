'''
    Given two singly linkedlist, write a program that takes this two
    cycle free singly linkedlists, and determine if there
    exist a node that is common to both lists.
'''
from ListNode import ListNode, create_linked_list, print_linked_list

def overlapping_no_cycle_lists(L1, L2):

    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    
    L1_len, L2_len = length(L1), length(L2)
    if L1_len > L2_len:
        L1, L2 = L2, L1 # L2 is the longer one.
    
    for _ in range(abs(L2_len - L1_len)):
        L2 = L2.next
    
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    
    return L1

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    f = ListNode(6)
    g = ListNode(7)
    h = ListNode(8)
    i = ListNode(9)
    j = ListNode(10)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    f.next = g
    g.next = e # overlap on node e.
    e.next = h
    h.next = i
    i.next = j

    print((overlapping_no_cycle_lists(a, f).data))