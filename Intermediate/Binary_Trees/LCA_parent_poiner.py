"""
    Design an algorithm which when given two nodes, output the LCA.
    imagine the binary tree has parent pointer.
    approach: Tandem move.
"""

def two_pointer_lca(node0, node1):
    # Helper func to calculate the depth.
    def get_depth(node):
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    dep0, dep1 = get_depth(node0), get_depth(node1)
    # Making node0 the deeper node to simplify the calculations in tandem
    if dep1 > dep0:
        node0, node1 = node1, node0

    dep_diff = abs(dep0 - dep1)
    while dep_diff:
        node0 = node0.parent

    # Moving in tandem to reach the common ancestor
    while node0 is not node1:
        node0, node1 = node0.parent, node1.parent

    return node0

