"""
    write a program to count the nodes of the tree
"""

def count(tree):
    if not tree:
        return 0
    return count(tree.left) + count(tree.right) + 1