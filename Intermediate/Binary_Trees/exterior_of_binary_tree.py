"""
    the Exterior of a binary tree is a sequence form the root to the leftmost leaf +
    from the leftmost leaf to the rightmost leaf + from rightmost leaf to the root.
    compute it. :)
"""

def exterior(tree):
    result = []
    stack = [tree]
    node = tree

    # root to left-most
    while node and node.left:
        result.append(node)
        node = node.left

    # leaves
    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            result.append(node)

        stack.append(node.right)
        stack.append(node.left)

    while tree and tree.right:
        tree = tree.right


