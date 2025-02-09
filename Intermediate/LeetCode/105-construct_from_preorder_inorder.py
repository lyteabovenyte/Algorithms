"""
    https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    node_to_idx = {data: i for i, data in enumerate(inorder)}

    def helper(inorder_start, inorder_end, preorder_start, preorder_end):
        if inorder_start >= inorder_end or preorder_start >= preorder_end:
            return

        root_idx_inorder = node_to_idx[preorder[preorder_start]]
        left_subtree_size = root_idx_inorder - inorder_start

        return (TreeNode(
            preorder[preorder_start],
            helper(
                inorder_start, root_idx_inorder,
                preorder_start + 1, preorder_start + 1 + left_subtree_size
            ),
            helper(
                root_idx_inorder + 1, inorder_end,
                preorder_start + 1 + left_subtree_size, preorder_end
            )
        ))

    return helper(0, len(inorder), 0, len(preorder))
