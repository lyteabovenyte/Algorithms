"""
    Given a preorder traversal of a tree with markers (`null` values are present).
    construct the actual tree.
"""
from BinaryTreeNode import BinaryTreeNode

def my_sol(preorder):
    stack = []

    for ele in preorder:
        curr = BinaryTreeNode(ele)

        if stack and stack[-1]:
            stack[-1].left = curr
        elif stack and stack[-1] is None:
            popped = stack.pop()
            assert popped.data is None
            popped2 = stack.pop()
            popped2.right = curr

        stack.append(curr)

    return stack[0]


tree = my_sol(["H", "B", "F", None, None, "E", "A", None, None, None, "C", None, "D", None,
                              "G", "I", None, None, None])

def print_tree(root):
    if root and root.data:
        print(root.data)
    if root.left:
        print_tree(root.left)
    if root.right:
        print_tree(root.right)

print_tree(tree)

#----

# recursive approach.
def recursive_preorder_with_marker(preorder):
    def reconstruct(preorder_iter):
        subtree_key = next(preorder_iter)
        if subtree_key is None:
            return None

        # note that reconstruct updates preorder_iter. so the
        # order of following two calls are critical.
        left_subtree = reconstruct(preorder_iter)
        right_subtree = reconstruct(preorder_iter)
        return BinaryTreeNode(subtree_key, left_subtree, right_subtree)

    return reconstruct(iter(preorder))
