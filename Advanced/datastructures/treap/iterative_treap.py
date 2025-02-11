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
        if node is not None:
            node.parent = self

    def set_right(self, node):
        self.right = node
        if node is not None:
            node.parent = self


class Treap:
    def __init__(self):
        self.root = None

    # ---- Utility Functions -----
    def _is_root(self, node):
        return node.parent is None
    
    def _is_leaf(self, node):
        return not node.left and not node.right

    # ---- Rotations -----
    def _rotate_right(self, node):
        """ right rotation for balancing"""
        if node is None or self._is_root(node):
            raise ValueError(f'Cannot rotate {node.key}. `Root` does not have `Parent` field.')
        y = node.parent
        assert y.left == node  # Right rotation can only be applied to left children
        p = y.parent

        if p is not None:
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

        if p is not None:
            if p.left == y:
                p.set_left(node)
            else:
                p.set_right(node)
        else:
            self.root = node

        y.set_right(node.left)
        node.set_left(y)

    # ------ Insert Operation ------
    def _insert(self, key, priority):
        node, parent = self.root, None
        new_node = TreapNode(key, priority)

        # first insert the node in the BST format.
        while node is not None: 
            # at the end of this loop, parent would point at a leaf.
            parent = node
            if key < node.key:
                node = node.left
            else:
                node = node.right

        if parent is None:
            self.root = new_node
            return
        elif key < parent.key:
            parent.set_left(new_node)
        else:
            parent.set_right(new_node)

        # then check for heap invariants
        while new_node.parent is not None and new_node.priority > new_node.parent.priority: 
            if new_node == new_node.parent.left:
                self._rotate_right(new_node)
            else:
                self._rotate_left(new_node)

        if new_node.parent is None:
            self.root = new_node

    def insert(self, key):
        self._insert(key, random.randint(0, 10**9))

    # ----- Search Operation -----
    def _search(self, node, target):
        if node is None:
            return None
        if node.key == target:
            return node
        elif target < node.key:
            return self._search(node.left, target)
        else:
            return self._search(node.right, target)

    def search(self, key):
        return self._search(self.root, key)

    # ------- Delete Operation -------
    def _delete(self, key) -> bool:
        node = self._search(self.root, key)
        if node is None:
            return False
        if self._is_root(node) and self._is_leaf(node):
            self.root = None
            return True
        
        while not self._is_leaf(node):
            if node.left and (node.right is None or node.right.priority < node.left.priority):
                    self._rotate_right(node.left)
            else:
                self._rotate_left(node.right)

            if self._is_root(node.parent):
                self.root = node.parent
            
        # at this point `node` is leaf and we disconnect it from its parent
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
        return True

    def delete(self, key):
        return self._delete(key)
    
    def top(self):
        if self.root is None:
            raise ValueError('Empty Treap.')
        key = self.root.key
        self._delete(key)
        return key

    def peek(self):
        return self.root.key
    
    def update(self, prev_key, new_key):
        node = self.search(prev_key)
        if not node:
            raise ValueError(f'Node {prev_key} not found.')
        node.priority = new_key
        if node.priority > node.parent.priority:
            while node.parent is not None:
                # we need to bubble up
                if node == node.parent.left:
                    self._rotate_right(node)
                else:
                    self._rotate_left(node)

        elif node.priority < max(node.left.priority, node.right.priority):
            # we need to push down
            while node is not None:
                if node.left and (node.right is None or node.right.priority < node.left.priority):
                    node._rotate_right(node.left)
                else:
                    node._rotate_left(node.right)

    def min(self):
        if self.root is None:
            raise Exception('Empty treap.')
        root_ = self.root
        while root_.left is not None:
            root_ = root_.left
        return root_.key

    def max(self):
        if self.root is None:
            raise Exception('Empty treap.')
        root_ = self.root
        while root_.right is not None:
            root_ = root_.right
        return root_.key