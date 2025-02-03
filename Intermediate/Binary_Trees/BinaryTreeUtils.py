import collections


class TreePath:
    def __init__(self, prev=None, to_left=False):
        self._prev = prev
        self._to_left = to_left

    def with_left(self):
        return TreePath(self, True)

    def with_right(self):
        return TreePath(self, False)

    def __str__(self):
        result = []
        node = self

        while node:
            result.append('->left' if node._to_left else '->right')
            node = node._prev

        result.reverse()
        result[0] = 'root'

        return ''.join(result)


def generate_preorder(tree):
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


def generate_inorder(tree):
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


def generate_postorder(tree):
    result = []
    s = [tree]

    while s:
        node = s.pop()
        if not node:
            continue

        result.append(node.data)
        s.append(node.left)
        s.append(node.right)

    result.reverse()

    return result


def find_node(tree, val):
    s = [tree]

    while s:
        node = s.pop()

        if not node:
            continue

        if node.data == val:
            return node

        s.append(node.left)
        s.append(node.right)

    return None


def must_find_node(tree, val):
    result = find_node(tree, val)
    if result is None:
        raise RuntimeError('{} was not found in the tree'.format(val))
    return result


def equal_binary_trees(tree1, tree2):
    s = [(tree1, tree2)]

    while s:
        node1, node2 = s.pop()

        if (node1 is None) != (node2 is None):
            return False

        if node1:
            if node1.data != node2.data:
                return False
            s.append((node1.left, node2.left))
            s.append((node1.right, node2.right))

    return True


def binary_tree_to_string(tree):
    result = ''
    nodes = collections.deque()
    visited = set()
    first = True
    null_nodes_pending = 0

    result += '['
    nodes.append(tree)

    while nodes:
        node = nodes.popleft()
        if id(node) in visited:
            raise RuntimeError('Detected a cycle in the tree')
        if node:
            if first:
                first = False
            else:
                result += ', '

            while null_nodes_pending:
                result += 'null, '
                null_nodes_pending -= 1

            result += '"{}"'.format(node.data)

            visited.add(id(node))
            nodes.append(node.left)
            nodes.append(node.right)
        else:
            null_nodes_pending += 1

    result += ']'
    return result


def binary_tree_height(tree):
    s = [(tree, 1)]
    height = 0

    while s:
        node, node_height = s.pop()
        if not node:
            continue

        height = max(height, node_height)
        s.append((node.right, node_height + 1))
        s.append((node.left, node_height + 1))

    return height


def binary_tree_size(tree):
    s = [tree]
    size = 0

    while s:
        node = s.pop()
        if not node:
            continue

        size += 1
        s.append(node.right)
        s.append(node.left)

    return size


# Python framework specific functions


def is_object_tree_type(tree):
    return tree and hasattr(tree, 'data') and \
           hasattr(tree, 'left') and hasattr(tree, 'right')


def convert_binary_tree_to_binary_tree_with_parent(tree):
    s = [(tree, None)]

    while s:
        node, parent = s.pop()
        if not node:
            continue

        node.parent = parent
        s.append((node.right, node))
        s.append((node.left, node))

    return tree


def strip_parent_link(tree):
    s = [tree]

    while s:
        node = s.pop()
        if node is None:
            continue

        node.parent = None
        s.append(node.left)
        s.append(node.right)
