'''
    Reverse a singly linked list.
'''
from main import Node, LinkedList
from ListNode import ListNode

def reverse(L):
    current = L.head
    prev = None
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    L.head = prev
    for ele in L:
        yield(ele)

# cooler implementation.
def reverse_list(head):
    dummy = ListNode(0)
    while head:
        dummy.next, head.next, head = head, dummy.next, head.next
    return dummy.next
    
l = LinkedList(["amir", "lyteabovenyte", "lyteatnyte"])
print(l.reverse())
