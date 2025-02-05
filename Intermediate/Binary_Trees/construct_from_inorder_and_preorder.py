"""
    Given inorder and preorder traversals of a binary tree, construct the tree itself.
    using hashmap to store nodes index in inorder traversal.
"""
from BinaryTreeNode import BinaryTreeNode as Btn

def construct_from_inorder_preorder(inorder, preorder):

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def construct_helper(inorder_start, inorder_end,
                         preorder_start, preorder_end):
        if inorder_end <= inorder_start or preorder_end <= preorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start

        return Btn(
            preorder[preorder_start],
            construct_helper(
                inorder_start, root_inorder_idx,
                preorder_start + 1, preorder_start + 1 + left_subtree_size
            ),
            construct_helper(
                root_inorder_idx + 1, inorder_end,
                preorder_start + 1 + left_subtree_size, preorder_end
            )
        )

    return construct_helper(0, len(inorder), 0, len(preorder))