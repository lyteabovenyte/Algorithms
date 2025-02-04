"""
    Compute the successor of the given node in an inorder traversal in binary tree.
    Assume the nodes contain parent field.
"""
def successor_inorder(tree, node):
    if not tree:
        return None

    if node.right:
        while node.left:
            node = node.left
        return node.data

    while node.parent and node.parent.right is node:
        node = node.parent
    return node.parent