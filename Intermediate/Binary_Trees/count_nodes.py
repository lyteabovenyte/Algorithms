"""
    write a program to count the nodes of the tree
"""

def count(tree):
    x, y = 0, 0
    while tree:
        x = count(tree.left)
        y = count(tree.right)
        return x + y + 1
    return