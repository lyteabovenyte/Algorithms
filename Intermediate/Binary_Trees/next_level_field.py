"""
    Assume that the nodes in a binary tree have a field called next_level,
    the next_level field contains a link to the right sibling of the node.
    Design and algorithm with traverse a binary tree and populate the next_level's field of each node
    and fill it with a link to it's right sibling's node.

    **complete binary tree only**
"""

def construct_right_sibling(tree):
    def populate_children_next_field(start_node):
        while start_node and start_node.left:
            # Populate left_child's next field.
            start_node.left.next = start_node.right
            # Populate right child's next field if iter is not the last node of the level
            start_node.right.next = start_node.next and start_node.next.left
            start_node = start_node.next

    while tree and tree.left:
        populate_children_next_field(tree)
        # this ensures that the process continues for each level,
        # moving down the left-most node (tree = tree.left).
        tree = tree.left