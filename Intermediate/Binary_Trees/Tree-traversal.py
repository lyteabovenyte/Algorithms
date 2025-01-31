"""
    Implementing the three variant of tree traversals.
    - The function call Stack reach at the max depth of the tree which variant between logn to n (logarithmic to
    linear
    - the actual representation of Tree traversal:
        - *Preorder* -> visit(node), Preorder(left), Preorder(right)
        - *Inorder* -> Inorder(left), visit(node), Inorder(right)
        - *Postorder* -> Postorder(left), Postorder(right), visit(node)
"""

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
