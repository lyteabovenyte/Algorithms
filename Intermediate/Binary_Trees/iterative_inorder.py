"""
    Inorder traversal without recursion.
    nodes doesn't have parent field
"""
from BinaryTreeNode import BinaryTreeNode as N

def iterative_inorder(tree):
    result = []
    stack = []
    node = tree

    while stack or node:

        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        result.append(node.data)

        node = node.right

    return result

tree = N(1, N(9, N(3, N(4, None, None),
                   None), N(5, None, None)),
         N(6, N(6, None, N(2, None, None))))

print(iterative_inorder(tree))



