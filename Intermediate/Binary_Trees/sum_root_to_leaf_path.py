"""
    consider a binary tree in which each node contain a binary digit, a root-to-leaf path
    can be associated with a binary number - the MSB is the root.
    Design an algorithm to compute the sum of the binary numbers represented by the root-to-leaf
    paths.

    approach: we can compute the sum of all root to leaf nodes as follows:
    Each time we visit a node, we compute the integer it encodes using the number of its parent.
    if the node is a leaf we return its integer, if it is not a leaf, we return the sum of the results
    from its left and right children.
"""
def sum_root_to_leaf_binary(tree, partial_path_sum=0):
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:
        return partial_path_sum

    return partial_path_sum(tree.left, partial_path_sum) + partial_path_sum(tree.right, partial_path_sum)
