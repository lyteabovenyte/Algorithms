from BinaryTreeNode import BinaryTreeNode as N
from BinaryTreeUtils import (binary_tree_to_string, generate_preorder,
                                generate_inorder)


tree = N(1, N(2, N(3, N(4, None, None),
                   None), N(5, None, None)),
         N(6, N(7, None, N(8, None, None))))

print(binary_tree_to_string(tree))



def preorder_iterator(root):
    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        if not node:
            continue

        result.append(node)
        stack.append(node.right)
        stack.append(node.left)
