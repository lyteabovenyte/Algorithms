"""
    Form a linked list from the leaves of a binary tree.
    keep the order from left to right.

    Approach:
    - we process the tree in preorder traversal, if the node is leaf we make it the next node
    in the result.
"""

# Iterative approach.
def linked_list_from_leaves(root):
    stack = [root]
    result = [] # contains the leave nodes with links to the other leave.

    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            if result:
                result[-1].next = node
            result.append(node)

        stack.append(node.right)
        stack.append(node.left)

    return result[0]

# Recursive approach.
def create_list_of_leaves(tree):
    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)