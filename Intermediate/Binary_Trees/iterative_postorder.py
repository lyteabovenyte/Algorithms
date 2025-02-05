"""
    Design an algorithm that generate the postorder traversals of a binary tree
    without recursion and parent field.
"""

# to generate the postorder traversal
# we can generate the Root-Right-Left and then reverse it.
def iterative_postorder(tree):
    result = []
    stack = [tree]

    while stack:
        node = stack.pop()
        if not node:
            continue

        result.append(node)
        stack.append(node.left)
        stack.append(node.right)

    result.reverse()
    return result
