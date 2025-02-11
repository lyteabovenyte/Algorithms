#### Treaps Notes - the best of two worlds, trees and heaps
- we can have the `search` of tree and the `top()` and `peek()` benefits of heaps
- How Treaps Work (Probabilistic Balancing)
  - Treaps are BSTs with an additional “priority” value for each node. These priority values are randomly assigned (typically drawn from a uniform distribution).
  - Each node follows two rules:
    - Binary Search Tree (BST) Property: Left child < Parent < Right child (based on key).
    - Heap Property: Parent has a higher priority than its children.
  - Key Idea: The random priority values determine the tree structure, not the insert order of keys! This randomization ensures balance in an expected way, rather than enforcing it explicitly.
  - worth noting that binary search trees offer the best average performance across all standard operations (`insert`, `delete`, `search`)
- A treap is equivalent to a randomized BST where each insertion order is randomly choosen.
- Unlike AVL trees or Red-Black trees, which strictly enforce balancing rules, a treap relies on *probability* for balance.
- By assigning random priorities, we are essentially simulating randomized *insertion* orders in a BST. A random BST is expected to have an  O(\log n)  height.
- In a treap, priorities determine the structure, not the order of insertion.
- Treaps are heaps, which in turn are special trees with a dual array representation. we can implement a heap using an array, a more space-efficient
representation that also exploits locality of reference.
- it’s important to note that rotations
always preserve BST constraints, but they do not preserve heap’s invariants. Rotations,
in fact, can be used to fix **broken treaps**, but if applied to a valid tree, they will break
the priority constraints on the node to which they are applied.
- in the `insert()` API of treaps, we have the ***rotations*** to fix the heap constraints.
- consider rotation on heaps:
```python
# rotation to the left is always applied to the right child (on x whose parent is p). 
def _rotate_left(node): # node is the parent of x.
  new_root = node.right
  node.right = new_right.right
  new_root.left = node
  return new_root

# rotation to the right is always applied on the left child.
def _rotate_right(node):
  new_root = node.left
  node.left = new_right.right
  new_root.right = node
  return new_root
```
- consider stack overflow on recursion method. although some programming language has *tail call optimization* on their compiler to return the recursion into iterative calls. (check for *tail call optimization* support on your programming language compiler)
- `search()` method in treap is the search method of BST.
- `insert()` in treap is just two step:
  - insert new_node as a leaf
  - if the priority is higher that it's parent, we take the subtree rooted at the parent and perform the needed rotation on that.

- [cp-algorithms treaps](https://cp-algorithms.com/data_structures/treap.html)
- 