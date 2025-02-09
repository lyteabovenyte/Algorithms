"""
    https://leetcode.com/problems/flatten-binary-tree-to-linked-list
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root

        stack = [root]
        dummy_node = TreeNode(0)
        prev = dummy_node

        while stack:
            node = stack.pop()
            

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            prev.right, prev.left = node, None
            prev = prev.right
            

        return dummy_node.right

        
