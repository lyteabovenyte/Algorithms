"""
    Write a program which returns the size of the largest complete subtree.
    A complete binary tree is a binary tree in which:
    - Every level, except possibly the last, is completely filled.
    - All nodes in the last level are as left as possible.

"""
import collections

def largest_subtree(tree):
    CompleteSubtreeWithSize = collections.namedtuple("CompleteSubtreeWithSize", (
        "size", "height", "is_complete"
    ))
    def dfs(root):
        if not root:
            return CompleteSubtreeWithSize(0, 0, True)

        ls, lh, lc = dfs(root.left)
        rs, rh, rc = dfs(root.right)

        # check if the current subtree is complete
        if lc and rc and (lh == rh or lh == rh + 1):
            size = ls + rs + 1
            height = max(lh, rh) + 1
            max_so_far[0] = max(max_so_far[0], size)
            return CompleteSubtreeWithSize(size, height, True)
        return CompleteSubtreeWithSize(0, 0, False)

    max_so_far = [0]
    dfs(tree)
    return max_so_far[0]

