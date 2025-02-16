import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.randint(1, 10 ** 9)  # Random priority for heap property
        self.left = None
        self.right = None


class Treap:
    def __init__(self):
        self.root = None

    # --- Utility Functions ---

    def _rotate_right(self, node):
        """ Right rotation for balancing Treap """
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        return new_root

    def _rotate_left(self, node):
        """ Left rotation for balancing Treap """
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root

    # --- Insert Operation ---

    """
        Combined of two operatins: 
        1. add the node to the leaf
        2. if the node's priority is greater than it's parent,
        take the subtree rooted at the parent and perform the needed rotation.
    """
    def _insert(self, node, key):
        """ Insert a key into the treap recursively """
        if node is None:
            return TreapNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
            if node.left.priority > node.priority:  # Heap property violated
                node = self._rotate_right(node)
        else:
            node.right = self._insert(node.right, key)
            if node.right.priority > node.priority:  # Heap property violated
                node = self._rotate_left(node)

        return node

    def insert(self, key):
        """ Public function to insert key """
        self.root = self._insert(self.root, key)

    # --- Delete Operation ---

    def _delete(self, node, key):
        """ Delete a key from the treap recursively """
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # If node has both children, rotate down the larger priority child
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                if node.left.priority > node.right.priority:
                    node = self._rotate_right(node)
                    node.right = self._delete(node.right, key)
                else:
                    node = self._rotate_left(node)
                    node.left = self._delete(node.left, key)

        return node

    def delete(self, key):
        """ Public function to delete key """
        self.root = self._delete(self.root, key)

    # --- Search Operation ---

    def _search(self, node, key):
        """
            Search for a key in the treap recursively
            Consider stack overflow for these kinds of recursion methods
            and also consider the tail call optimization if it is supported
            in programming languages compiler.
        """
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def search(self, key):
        """ Public function to search for key """
        return self._search(self.root, key)

    # --- Split and Merge Operations (Used for Advanced Use Cases) ---

    def _split(self, node, key):
        """ Splits the Treap into two trees: left <= key, right > key """
        if node is None:
            return None, None
        elif key < node.key:
            left, node.left = self._split(node.left, key)
            return left, node
        else:
            node.right, right = self._split(node.right, key)
            return node, right

    def _merge(self, left, right):
        """ Merges two treaps into one """
        if left is None or right is None:
            return left if left is not None else right

        if left.priority > right.priority:
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right

    # --- Inorder Traversal (for debugging) ---

    def inorder_traversal(self, node=None, result=None):
        """ Returns sorted list of keys (BST property check) """
        if result is None:
            result = []
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left, result)
        result.append(node.key)
        if node.right:
            self.inorder_traversal(node.right, result)
        return result