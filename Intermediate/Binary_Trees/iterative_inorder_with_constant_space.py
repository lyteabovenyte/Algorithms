"""
    in both recursive and iterative (using stack) version of inorder traversals, the space
    complexity remains O(h) -> height of the tree.
    Design a non-recursive algorithm which computes the inorder traversal of a binary tree.
    Assume that each node have a link to its parent.
"""
def iterative_inorder_constant_space(tree):
    prev, result = None, []
    while tree:
        if prev is tree.parent:
            # we came down from prev to tree
            if tree.left:
                next_ = tree.left
            else:
                result.append(tree.data)
                next_ = tree.right or tree.parent

        elif tree.left is prev:
            # we came up to the tree from it's left child
            result.append(tree.data)
            next_ = tree.right or tree.parent
        else: # Done with both children
            next_ = tree.parent

        prev, tree = tree, next_

    return result