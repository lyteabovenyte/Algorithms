"""
    https://leetcode.com/problems/sum-root-to-leaf-numbers
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def helper(tree, partial_int=0):
            if not tree:
                return 0
            
            partial_int = partial_int * 10 + tree.val
            if not tree.left and not tree.right:
                return partial_int
            
            return (helper(tree.left, partial_int) + helper(tree.right, partial_int))
        
        return helper(root, 0)