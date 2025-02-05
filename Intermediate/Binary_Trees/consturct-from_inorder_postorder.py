"""
    Given the inorder and postorder traversal of binary tree,
    construct the tree itself.
"""
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    if not inorder or not postorder:
        return None

    # Create a hashmap to quickly locate root index in inorder traversal
    inorder_index_map = {val: idx for idx, val in enumerate(inorder)}

    # Postorder index tracker (last element is root initially)
    post_idx = [len(postorder) - 1]

    # Recursive function to construct the tree
    def construct(left: int, right: int) -> Optional[TreeNode]:
        if left > right:
            return None

        # Get the root value from postorder
        root_val = postorder[post_idx[0]]
        root = TreeNode(root_val)

        # Move to the next postorder index (right to left)
        post_idx[0] -= 1

        # Get the index of the root in the inorder list
        inorder_root_index = inorder_index_map[root_val]

        # Recursively build right subtree first (since postorder is L R Root)
        root.right = construct(inorder_root_index + 1, right)
        root.left = construct(left, inorder_root_index - 1)

        return root

    return construct(0, len(inorder) - 1)