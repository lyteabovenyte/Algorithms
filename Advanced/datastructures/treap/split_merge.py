import random

class TreapNode:
    def __init__(self, key, priority=None):
        self.key = key
        self.priority = priority if priority is not None else random.randint(1, 10**9)
        self.left = None
        self.right = None

def split(root, key):
    """Splits treap into two treaps: left (≤ key) and right (> key)."""
    if root is None:
        return None, None

    if root.key <= key:
        left, right = split(root.right, key)
        root.right = left  # Assign split left to root's right
        return root, right
    else:
        left, right = split(root.left, key)
        root.left = right  # Assign split right to root's left
        return left, root

def merge(left, right):
    """Merges two treaps into a single valid treap."""
    if left is None:
        return right
    if right is None:
        return left

    if left.priority > right.priority:
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right
    