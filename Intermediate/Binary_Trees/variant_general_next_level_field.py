"""
    populating next_level field (pointing to the right sibling) for a general binary tree.
"""
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root):
    # BFS like approach. populating level-by-level using Queue
    queue = deque([root])
    
    while queue:
        size = len(queue)
        prev = None

        for _ in range(size):
            node = queue.popleft()

            if prev:
                prev.next = node
            prev = node

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        prev.next = None
        
    return root


def connect(root):
    if not root:
        return None

    leftmost = root  # Start from the leftmost node of the first level

    while leftmost:
        dummy = Node(0)  # Dummy node to track the start of the next level
        curr = dummy  # Pointer to connect the next level's nodes
        
        temp = leftmost  # Traverse the current level
        while temp:
            if temp.left:
                curr.next = temp.left  # Connect left child
                curr = curr.next
            if temp.right:
                curr.next = temp.right  # Connect right child
                curr = curr.next
            temp = temp.next  # Move to next node in current level
        
        leftmost = dummy.next  # Move to next level

    return root