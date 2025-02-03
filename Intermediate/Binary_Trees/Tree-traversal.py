"""
    Implementing the three variant of tree traversals.
    - The function call Stack reach at the max depth of the tree which variant between logn to n (logarithmic to
    linear
    - the actual representation of Tree traversal:
        - *Preorder* -> visit(node), Preorder(left), Preorder(right)
        - *Inorder* -> Inorder(left), visit(node), Inorder(right)
        - *Postorder* -> Postorder(left), Postorder(right), visit(node)
"""
from BinaryTreeNode import BinaryTreeNode as N

def tree_traversal(root):
    def preorder(root):
        print(f'preorder: {root.data}')
        preorder(root.left)
        preorder(root.right)
    

    def inorder(root):
        inorder(root.left)
        print(f'inorder: {root.data}')
        inorder(root.right)

    def postorder(root):
        postorder(root.left)
        postorder(root.right)
        print(f'Postorder: {root.data}')


# Iterative version of Tree traversals
def preorder(tree):
    result = []
    s = [tree]

    while s:
        node = s.pop()
        if not node:
            continue

        result.append(node.data)
        s.append(node.right)
        s.append(node.left)

    return result


def better_iterative_inorder_traversal(tree):
    result = []
    stack = []
    node = tree  # Start from the root

    while stack or node:
        # Step 1: Reach the leftmost node
        while node:
            stack.append(node)
            node = node.left

        # Step 2: Process the node
        node = stack.pop()
        result.append(node.data)

        # Step 3: Move to the right subtree
        node = node.right

    return result

def inorder(tree):
    result = []
    s = [tree]
    initial = True

    if not tree:
        return result

    while s:
        node = s.pop()

        if initial:
            initial = False
        else:
            result.append(node.data)
            node = node.right

        while node:
            s.append(node)
            node = node.left

    return result

# to achieve the left-right-root we can generate
# root-right-left and then reverse it.
def postorder(tree):
    result = []
    s = [tree]

    while s:
        node = s.pop()
        if not node:
            continue

        result.append(node)
        s.append(node.left)
        s.append(node.right)

    result.reverse()
    return result


tree = N(1, N(2, N(4), N(5, N(8), None)),
             N(3, N(6, None, N(9)), N(7, None, N(10, N(11), N(12)))))

tree2 = N(1, N(2, N(3, None, None), N(4, N(5, None, None), None)
              ), N(6, None, N(7, N(8, None, None), N(9, None, None))))

print(inorder(tree))
print(better_iterative_inorder_traversal(tree2))
