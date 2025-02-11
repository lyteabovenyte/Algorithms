from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # inorder traversal should be ordered.
        stack, inorder = [], []
        node = root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            inorder.append(node.val)
            node = node.right

        return inorder == list(sorted(inorder))


# another approach
def is_valid_bst(root):

    def helper(root, min_, max_): 
        if not root:
            return True
        
        if (not root.val > min_ and root.val < max_):
            return False
        
        return helper(root.left, min_, root.val) and (root.right, root.val, max_)
    
    return helper(root, float('-inf'), float('inf'))
