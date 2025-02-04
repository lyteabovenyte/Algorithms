"""
    Implement preorder traversal without recursion. ( iterative means with loops )
"""

def iterative_preorder(tree):
    stack, result = [tree], []

    while stack:
        node = stack.pop()
        if not node:
            continue

        result.append(node.data)
        stack.append(node.right)
        stack.append(node.left)

    return result


