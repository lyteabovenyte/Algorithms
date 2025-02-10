"""
    https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        from collections import namedtuple
        Status = namedtuple('Status', ("num_target_nodes", "ancestor"))

        def helper(root, p, q):
            if not root:
                return Status(0, None) 

            left = helper(root.left, p, q)
            if left.num_target_nodes == 2:
                return left
            
            right = helper(root.right, p, q)
            if right.num_target_nodes == 2:
                return right
            
            num_tar_nodes = (left.num_target_nodes + right.num_target_nodes +
                            (p.val, q.val).count(root.val))
            return Status(num_tar_nodes, root.val if num_tar_nodes == 2 else None)
        
        return helper(root, p, q).ancestor


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: 
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root # Found
        
        return left if left else right
        


