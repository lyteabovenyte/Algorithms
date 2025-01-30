"""
    Given a binary tree with integer keys, write a program which return the average of each depth keys
"""
import functools

def avg_depth_binary_tree(tree):
    result = []

    curr_depth_nodes = [tree]

    while curr_depth_nodes:
        result.append([functools.reduce(lambda x, y: x + y, curr_depth_nodes, 0)])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes for child in (curr.left, curr.right)
            if child
        ]
    return result