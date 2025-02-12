"""
    https://leetcode.com/problems/kth-smallest-element-in-a-bst
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inorder, stack = [], []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            inorder.append(node.val)

            node = node.right
            
        return inorder[k - 1]
