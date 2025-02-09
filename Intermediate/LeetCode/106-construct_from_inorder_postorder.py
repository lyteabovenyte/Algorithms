"""
    https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    node_to_idx = {data: i for i, data in enumerate(inorder)}

    post_idx = [len(postorder) - 1]

    def helper(left, right):
        if left >= right:
            return None

        root_val = postorder[post_idx[0]]
        root = TreeNode(root_val)
        post_idx[0] -= 1

        inorder_root_idx = node_to_idx[root_val]


        root.right = helper(inorder_root_idx + 1, right)
        root.left = helper(left, inorder_root_idx - 1)

        return root

    return helper(0, len(inorder) - 1)