"""
    Write a program which returns the size of the largest subtree.
"""
def largest_subtree(tree):
    if not tree:
        return 0
    max_size_so_far = 0

    def size(tree):
        if not tree:
            return 0
        return size(tree.left) + size(tree.right) + 1

    def is_complete(tree):
        if tree.left and tree.right:
            return True
        return False

    left_subtree = is_complete(tree.left)
    if left_subtree:
        max_size_so_far = max(size(tree.left), max_size_so_far)

    right_subtree = is_complete(tree.right)
    if right_subtree:
        max_size_so_far = max(size(tree.right))

    return max_size_so_far
