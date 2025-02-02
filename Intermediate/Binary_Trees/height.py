"""
    write a program that compute the height of a tree.
"""

def height(tree):
    x, y = 0, 0
    while tree:
        x = height(tree.left)
        y = height(tree.right)
        if (x > y):
            return x + 1
        else:
            return y + 1
    return
