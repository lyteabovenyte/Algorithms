"""
    Design an algorithm for computing the LCA(lowest-common-ancestor) of two nodes in a binary tree in which nodes do not
    have a parent field
    - when is the root the LCA?
"""
from BinaryTreeNode import BinaryTreeNode as N

def LCA(tree, value1, value2):

    def _search_recursive(root, a, b):
        if not root:
            return False
        if root.data == a or root.data == b:
            return True
        return _search_recursive(root.left, a, b) or _search_recursive(root.right, a, b)


    def dfs(root, x, y):

        left_sub  = _search_recursive(root.left, x, y)
        right_sub = _search_recursive(root.right, x, y)

        if not left_sub:
            root = root.right
            if root.data == x or y:
                return root.data
            return dfs(root, x, y)

        elif not right_sub:
            root = root.left
            if root.data == x or y:
                return root.data
            return dfs(root, x, y)
        else:
            return root.data

    return dfs(tree, value1, value2)

tree = N(1, N(2), N(5, N(6,
                         N(7, None, N(8)), None), N(9, N(10), None)))
print(LCA(tree, 10, 9))

"""
    the program below returns and object with two fields
    the first is an integer indication how many of the two
    nodes were present in that subtree, and the second is their LCA
    if both nodes were present
    somewhat similar to recursive postorder traversal.
"""
import collections

def lowest_common_ancestor(tree, node0, node1):
    Status = collections.namedtuple('Status', ("num_target_nodes", "ancestor"))

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result

        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            return right_result

        num_target_nodes = (left_result.num_target_nodes + right_result.num_target_nodes +
                            (node0, node1).count(tree.data))
        return Status(num_target_nodes, tree if num_target_nodes == 2
                      else None)

    return lca_helper(tree, node0, node1).ancestor

print(lowest_common_ancestor(tree, 6, 8))


























