"""
    Compute the kth node in a binary tree in inorder traversal.
"""
from BinaryTreeNode import BinaryTreeNode as N

# Time Complexity: O(n)
def kth_node_inorder(tree, k):
    stack, node = [], tree

    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        k -= 1
        if k == 0:
            return node.data
        node = node.right
    return 0

tree = N(1, N(9, N(3, N(4, None, None),
                   None), N(5, None, None)),
         N(6, N(6, None, N(2, None, None))))
print(kth_node_inorder(tree, 8))  # 6

# Can we do better?
# what if we had the size of each node (the number of nodes, rooted at that specific node.
