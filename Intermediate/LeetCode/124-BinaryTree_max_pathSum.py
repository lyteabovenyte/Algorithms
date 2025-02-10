"""
    https://leetcode.com/problems/binary-tree-maximum-path-sum
    level: Hard
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = float("-inf")

        def get_max_path(node):
            nonlocal max_path
            if node is None:
                return 0
            
            gain_on_left = max(get_max_path(node.left), 0)
            gain_on_right = max(get_max_path(node.right), 0)

            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return node.val + max(gain_on_left, gain_on_right)
        
        get_max_path(root)
        return max_path