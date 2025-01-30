"""
    Given a binary tree, write a program to return the nodes, on the bottom to top, left to rigth
    order.
"""
# we could just generate keys, in top-down, right-to-left and reverse it.
def bottom_to_top_tree(tree):
    result = []
    if not tree:
        return result

    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
            child
            for curr in curr_depth_nodes for child in (curr.right, curr.left)
            if child
        ]

    return  list(reversed([list(reversed(ele)for ele in result]))