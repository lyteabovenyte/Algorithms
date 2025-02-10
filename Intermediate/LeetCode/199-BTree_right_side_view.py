"""
    https://leetcode.com/problems/binary-tree-right-side-view
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS using queue.
        from collections import deque
        q = deque([root])

        result = []

        while q:
            size = len(q)

            for _ in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            result.append(node.val)

        return result
            
            
            