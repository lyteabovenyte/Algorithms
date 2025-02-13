"""
    https://leetcode.com/problems/binary-search-tree-iterator
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.result = []
        self.pointer = -1
        self.inorder_iter(root)

    def inorder_iter(self, root):
        stack = []
        node = root

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else: 
                node = stack.pop()
                self.result.append(node.val)
                node = node.right
        
    def next(self) -> int:
        self.pointer += 1
        return self.result[self.pointer]

    def hasNext(self) -> bool:
        if self.pointer < len(self.result) - 1:
            return True
        else:
            return False

