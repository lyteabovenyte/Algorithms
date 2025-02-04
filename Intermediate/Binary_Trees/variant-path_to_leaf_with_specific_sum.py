"""
    Given a binary tree whose nodes contain integer numbers and an integer k,
    return all the paths to the leaves whose path weights equal to k.
    suppose the path weight of such a tree is the sum of the integers on
    unique path from the root to that node.
"""
from BinaryTreeNode import BinaryTreeNode as N
def variant_path_to_leaf_sum(root, k):
    result = []

    def path_to_leaf_helper(node, remaining_weight, partial_res):
        if not node:
            return

        # Include current node in the path
        partial_res.append(node.data)

        # Check if it's a leaf and the sum matches k
        if not node.left and not node.right and remaining_weight == node.data:
            result.append(list(partial_res))  # Append a copy

        # Recur for left and right children
        path_to_leaf_helper(node.left, remaining_weight - node.data, partial_res)
        path_to_leaf_helper(node.right, remaining_weight - node.data, partial_res)

        # Backtrack
        partial_res.pop()

    path_to_leaf_helper(root, k, [])
    return result


tree = N(1, N(9, N(3, N(4, None, None),
                   None), N(5, None, None)),
         N(6, N(6, None, N(2, None, None))))

print(variant_path_to_leaf_sum(tree, 15)) # [[1, 9, 5], [1, 6, 6, 2]]