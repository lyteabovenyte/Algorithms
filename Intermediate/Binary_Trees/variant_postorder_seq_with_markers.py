"""
    Given a modified version of postorder sequence of a binary tree (with None nodes determined),
    construct the binary tree.
"""
from BinaryTreeNode import BinaryTreeNode

# catch: postorder's reversed is root, right, left
def postorder_with_markers(postorder):
    postorder.reverse()

    def construct(postorder_iter):
        subtree_key = next(postorder_iter)
        if subtree_key is None:
            return None

        right_subtree = construct(postorder_iter)
        left_subtree = construct(postorder_iter)
        return BinaryTreeNode(subtree_key, right_subtree, left_subtree)

    return construct(iter(postorder))