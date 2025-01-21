'''
    Reverse a singly linked list.
'''
from main import Node, LinkedList

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
    

l = LinkedList(["amir", "lyteabovenyte", "lyteatnyte"])
print(l.reverse())
