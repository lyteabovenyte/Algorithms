"""
    https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
"""
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        from collections import deque
        q = deque([root])
        direction = 1
        final_res = []


        while q:
            size = len(q)
            res = []
            direction += 1

            for _ in range(size):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if direction % 2 == 0:
                final_res.append(res)
            else:
                final_res.append(list(reversed(res)))

        return final_res