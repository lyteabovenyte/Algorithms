"""
    Given the edges of a binary tree (links between nodes), find the root of the binary tree.
"""

def find_root(edges):
    all_nodes, child_nodes = set(), set()

    for parent, child in edges:
        all_nodes.add(parent)
        all_nodes.add(child)
        child_nodes.add(child)

    # root is the only node, that is in the all_nodes, but is not in the child_nodes set.
    root = (all_nodes - child_nodes).pop()
    return root

edges = [(5, 3), (5, 8), (3, 1), (3, 4), (8, 6), (8, 7)]
print(find_root(edges))

