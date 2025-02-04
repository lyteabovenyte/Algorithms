"""
    output the kth node in an inorder traversal.
    privilege: Assume that each node stores the number of nodes rooted at that node.
"""
# time complexity: O(h)
def privilege_kth_node(tree, k):
    while tree:
        left_size = tree.left.data if tree.left else 0

        if left_size + 1 < k: # k is in the right subtree
            k -= left_size + 1
            tree = tree.right
        elif left_size + 1 == k: # k is the iter itself
            return tree
        else:
            tree = tree.left
    return None