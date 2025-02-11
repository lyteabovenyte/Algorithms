"""
    Testing my treaps knowledge on implementing a Treap class and all of it's API methods
"""
import random

class TreapNode:
    def __init__(self, key, priority=random.randint(0, 10**9)):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None
        self.parent = None   # serving parent link to simplify the API methods

    def set_left(self, node):
        self.left = node
        if node != None:
            node.parent = self

    def set_right(self, node):
        self.right = node
        if node != None:
            node.parent = self




class Treap:

    def __init__(self):
        self.root = None

    # ---- Utility Functions -----

    def _is_root(self, node):
        if node.parent == None:
            return True
        return False

    # ---- Rotations -----
    """
        Note how we manage the parent field
        in each rotation.
    """
    def _rotate_right(self, node):
        """ right rotation for balancing"""
        if node is None or self._is_root(node):
            raise ValueError(f'Cannot rotate {node.key}. `Root` does not have `Parent` field.')
        y = node.parent
        assert y.left != node  # Right rotation can only be applied to left childrens
        p = y.parent

        if p != None:
            if p.left == y:
                p.set_left(node)
            else:
                p.set_right(node)
        else:
            self.root = node

        y.set_left(node.right)
        node.set_right(y)

    def _rotate_left(self, node):
        if node is None or self._is_root(node):
            raise ValueError(f'Cannot rotate {node.key}. `Root` does not have `Parent` field')
        y = node.parent
        assert y.right == node
        p = y.parent

        if p != None:
            if p.left == y:
                p.set_left(node)
            else:
                p.set_right(node)
        else:
            self.root = node

        y.set_right(node.left)
        node.set_left(y)

    
    # ------ Insert Operation ------
    """
        Insert operation comes in two steps:
        1. Insert at the leaf (like Binary tree)
        we keep track of the parent node
        to be able to add the new_node as the child of leaf.
        2. check heap invariants, if violated, 
        rotate the subtree rooted at the parent node
    """
    def _insert(self, key, priority):
        node, parent = self.root, None
        new_node = TreapNode(key, priority)

        # first insert the node in the BST format.
        while node is not None: 
            # at the end of this loop, parent would point at a leaf.
            parent = node
            if node.key <= key:
                node = node.left
            else:
                node = node.right

        if parent is None:
            self.root = new_node
            return
        elif key <= parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.parent = parent
        # then check for heap invariants
        while new_node.parent != None:
            if new_node.priority < new_node.parent.priority: # Min-Heap
                if new_node == new_node.parent.left:
                    self._rotate_right(new_node)
                else:
                    self._rotate_left(new_node)

        if new_node.parent == None:
            # in this case we need to update
            # our Treap's root value to new_node
            self.root = new_node
        

        # ----- Search Operation -----

        def _search(self, node, target): # `node` is the starting point (root) for search
            if node== None:
                return None
            if node.key == target:
                return node
            elif target < node.key:
                return self._search(node.left, target)
            else:
                return self._search(node.right, target)


        # ------- Delete Operation -------
        """
            with respect to BST and it's delete operation
            it is conceptually different.
            we assign the least priority to the node, and push it down
            until it reaches the leaf, so we easily remove it.
        """
        def _delete(self, key) -> bool:
            node = self._search(self.root, key)
            
