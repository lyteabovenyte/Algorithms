"""
    define a node in a binary tree to be k-balanced if the difference in the number of nodes in it's
    left and right subtree is no more than k. design an algorithm that takes as input a binary tree
    and a positive integer k, and returns a node in the binary tree such that the node is
    not k-balanced, but all its descendants are k-balanced.
"""
# Approach: bottom-up, because we want to find the lowest node which violates the condition
# but its descendants are good.

from BinaryTreeNode import BinaryTreeNode as N

def find_unbalanced_node(root, k):
    def dfs(node):
        if not node:
            return 0, None

        left_size, left_unbalanced = dfs(node.left)
        right_size, right_unbalanced = dfs(node.right)
        subtree_size = left_size + right_size + 1   # calculate the size.

        # if we find an unbalanced node, immediately return it
        if left_unbalanced:
            return subtree_size, left_unbalanced
        if right_unbalanced:
            return subtree_size, right_unbalanced

        if abs(left_size - right_size) > k:
            return subtree_size, node  # current node is unbalanced

        return subtree_size, None  # otherwise return nothing

    _, _unbalanced_node = dfs(root)
    return _unbalanced_node.data, _unbalanced_node.left, _unbalanced_node.right

tree = N(1, N(2, N(4), N(5, N(8), None)),
             N(3, N(6, None, N(9)), N(7, None, N(10, N(11), N(12)))))

print(find_unbalanced_node(tree, 2))