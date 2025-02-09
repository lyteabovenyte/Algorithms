"""
    https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Using BFS like approach.
        # level-by-level traversal using Queue.
        from collections import deque
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



        

