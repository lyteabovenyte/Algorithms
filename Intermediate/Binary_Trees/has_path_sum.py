"""
    Given a binary tree and an integer k, suppose the path weight of such a tree is the sum of the integers on
    unique path from the root to that node.
    Design an algorithm which takes as input an integer and a binary tree with integer node weights, and
    check if there exists a leaf whose path weight equals the given integer k.
"""
def has_path_sum(tree, remaining_weight):
    if not tree:
        return False

    if not tree.left and not tree.right:
        return remaining_weight == tree.data

    return (has_path_sum(tree.left, remaining_weight - tree.data) or
           has_path_sum(tree.right, remaining_weight - tree.data))
