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

def buildTree2(inorder: List[int], postorder: List[int]) -> TreeNode:
    rec = {val: i for i, val in enumerate(inorder)}

    # Helper function
    def helper(in_start: int, in_end: int, post_start: int, post_end: int):
        if in_start > in_end or post_start > post_end:
            return None

        val = postorder[post_end]
        root = TreeNode(val)
        idx = rec[val]
        left_subtree_size = idx - in_start

        # Recursively build left and right subtrees
        root.left = helper(in_start, idx - 1, post_start, post_start + left_subtree_size - 1)
        root.right = helper(idx + 1, in_end, post_start + left_subtree_size, post_end - 1)

        return root

    return helper(0, len(inorder) - 1, 0, len(postorder) - 1)