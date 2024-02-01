'''
    implementing a LinkedList
'''

class ListNode:
    
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node
        
    '''
        impelementing the basik list API -search, insert, delete- for singly linkedlist
    '''
    
    def search_list(L, key):
        while L and L.data != key:
            L = L.next
        # if key was not found in the list, L will have become null
        return L
    
    
    def insert_after(node, new_node):
        '''
            insert a new node after a specified node
        '''
        new_node.next = node.next
        node.next = new_node
        
        
    def delete_after(node):
        '''
            delete the node past this one, Assume node is not a tail
        '''
        node.next = node.next.next 
        