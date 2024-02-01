from ListNode import ListNode #represented on the same directory on file ListNode.py
'''
class ListNode:
    
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
        
        .
        .
        .
''' 
        
        
def merge_two_sorted_linkedlist(L1, L2):
    
    # create a placeholder for result
    dummy_head = tail = ListNode()
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next 
        else:
            tail.next, L2 = L2, L2.next 
            
    tail.next = L1 or L2
    return dummy_head.next
    
