"""
    https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        from collections import deque
        q = deque([root])
        res = []
        while q:
            size = len(q)
            running_sum = 0

            for _ in range(size):
                node = q.popleft()
                running_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            answer = running_sum / size
            res.append(answer)
            
        return res