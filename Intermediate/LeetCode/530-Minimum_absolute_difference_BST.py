from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        inorder, stack = [], []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            inorder.append(node.val)
            node = node.right

        i, j, min_ = 0, 1, float('inf')
        while j < len(inorder):
            min_ = min(inorder[j] - inorder[i], min_)
            i, j = i + 1, j + 1
        return min_
