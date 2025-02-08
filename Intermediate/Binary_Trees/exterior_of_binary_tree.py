"""
    the Exterior of a binary tree is a sequence form the root to the leftmost leaf +
    from the leftmost leaf to the rightmost leaf + from rightmost leaf to the root.
    compute it. :)
"""

def exterior(tree):

    def is_leaf(node):
        return node if not node.left and not node.right else []

    # Compute the nodes from the root to the leftmost leaf followed by all
    # the leaves in subtree
    def left_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []

        return (([subtree] if is_boundary
                 or is_leaf(subtree) else []) + left_boundary_and_leaves(
            subtree.left, is_boundary) + left_boundary_and_leaves(
            subtree.right, is_boundary and not subtree.left))

    def right_boundary_and_leaves(subtree, is_boundary):
        if not subtree:
            return []

        return (right_boundary_and_leaves(subtree.left, is_boundary and not subtree.right) +
                right_boundary_and_leaves(subtree.right, is_boundary) +
                ([subtree] if is_boundary or is_leaf(subtree) else []))

    return ([tree] + left_boundary_and_leaves(tree.left, is_boundary=True) +
            right_boundary_and_leaves(tree.right, is_boundary=True) if tree else [])


