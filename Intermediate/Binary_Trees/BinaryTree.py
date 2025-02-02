class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root_value=None):
        self.root = TreeNode(root_value) if root_value is not None else None

    # insertion happens in a Binary Tree using Queue.
    def insert(self, value):
        """Inserts a value into the tree using level-order (BFS) insertion."""
        if not self.root:
            self.root = TreeNode(value)
            return

        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left:
                node.left = TreeNode(value)
                return
            else:
                queue.append(node.left)

            if not node.right:
                node.right = TreeNode(value)
                return
            else:
                queue.append(node.right)

    def search(self, value):
        """Searches for a value in the tree (DFS)."""
        return self._search_recursive(self.root, value)

    # search for existence.
    def _search_recursive(self, node, value):
        if not node:
            return False
        if node.value == value:
            return True
        return self._search_recursive(node.left, value) or self._search_recursive(node.right, value)

    def delete(self, value):
        """Deletes a node by replacing it with the deepest rightmost node."""
        if not self.root:
            return None

        queue = [self.root]
        key_node = None
        parent = None
        last_node = None

        while queue:
            parent = last_node
            last_node = queue.pop(0)

            if last_node.value == value:
                key_node = last_node

            if last_node.left:
                queue.append(last_node.left)

            if last_node.right:
                queue.append(last_node.right)

        if key_node:
            key_node.value = last_node.value  # Replace value
            self._delete_deepest(self.root, last_node)

    def _delete_deepest(self, root, d_node):
        """Deletes the deepest node."""
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is d_node:
                node = None
                return
            if node.right:
                if node.right is d_node:
                    node.right = None
                    return
                queue.append(node.right)
            if node.left:
                if node.left is d_node:
                    node.left = None
                    return
                queue.append(node.left)

    def inorder_traversal(self):
        """Performs in-order traversal (Left-Root-Right)."""
        result = []
        self._inorder_helper(self.root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)

    def preorder_traversal(self):
        """Performs pre-order traversal (Root-Left-Right)."""
        result = []
        self._preorder_helper(self.root, result)
        return result

    def _preorder_helper(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_helper(node.left, result)
            self._preorder_helper(node.right, result)

    def postorder_traversal(self):
        """Performs post-order traversal (Left-Right-Root)."""
        result = []
        self._postorder_helper(self.root, result)
        return result

    def _postorder_helper(self, node, result):
        if node:
            self._postorder_helper(node.left, result)
            self._postorder_helper(node.right, result)
            result.append(node.value)

    def level_order_traversal(self):
        """Performs level-order traversal (BFS)."""
        if not self.root:
            return []

        queue = [self.root]
        result = []
        while queue:
            node = queue.pop(0)
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def height(self, node=None):
        """Computes the height of the tree."""
        if node is None:
            node = self.root
        if not node:
            return -1  # Height of an empty tree is -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def is_balanced(self, node=None):
        """Checks if the tree is balanced."""
        if node is None:
            node = self.root
        if not node:
            return True

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.is_balanced(node.left) and self.is_balanced(node.right)

    def find_min(self):
        """Finds the minimum value in the tree (assuming it's a BST)."""
        node = self.root
        while node and node.left:
            node = node.left
        return node.value if node else None

    def find_max(self):
        """Finds the maximum value in the tree (assuming it's a BST)."""
        node = self.root
        while node and node.right:
            node = node.right
        return node.value if node else None

    def count_nodes(self):
        """Counts the total number of nodes."""
        return self._count_nodes_helper(self.root)

    def _count_nodes_helper(self, node):
        if not node:
            return 0
        return 1 + self._count_nodes_helper(node.left) + self._count_nodes_helper(node.right)

    def is_full_binary_tree(self, node=None):
        """Checks if the tree is a full binary tree (every node has 0 or 2 children)."""
        if node is None:
            node = self.root
        if not node:
            return True
        # the XOR condition.
        if (node.left is None and node.right is not None) or (node.left is not None and node.right is None):
            return False
        return self.is_full_binary_tree(node.left) and self.is_full_binary_tree(node.right)


# Example Usage
bt = BinaryTree()
bt.insert(10)
bt.insert(5)
bt.insert(15)
bt.insert(3)
bt.insert(7)
bt.insert(12)
bt.insert(18)

print("In-order Traversal:", bt.inorder_traversal())  # [3, 5, 7, 10, 12, 15, 18]
print("Pre-order Traversal:", bt.preorder_traversal())  # [10, 5, 3, 7, 15, 12, 18]
print("Post-order Traversal:", bt.postorder_traversal())  # [3, 7, 5, 12, 18, 15, 10]
print("Level-order Traversal:", bt.level_order_traversal())  # [10, 5, 15, 3, 7, 12, 18]
print("Tree Height:", bt.height())  # 2
print("Is Balanced:", bt.is_balanced())  # True
print("Min Value:", bt.find_min())  # 3
print("Max Value:", bt.find_max())  # 18
print("Total Nodes:", bt.count_nodes())  # 7
print("Is Full Binary Tree:", bt.is_full_binary_tree())  # True