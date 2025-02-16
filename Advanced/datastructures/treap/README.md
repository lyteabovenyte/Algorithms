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
- from the book itself: (advanced data structure and algorithms)
```
We’ll see in the next chapters, and in particular in chapter 7, when we talk about
cache, that there are better ways to address problems equivalent to the example we
presented in this chapter.
Let me be clear: using treaps as both trees and heaps is possible, perfectly legal,
and can even offer decent performance, under certain conditions, although in the
general case we have seen that keeping data organized by both criteria will likely pro-
duce an unbalanced tree (which means linear-time operations).
But that’s not why treaps were invented, nor is it the main way they are used today.
In the end, the point is that there are better ways to index multidimensional data and
better ways to use treaps. Instead, we’ll see that we can use treaps as a building block
to implement a different, and efficient, data structure.
```

- difference between *accuracy*, *precision* and *recall*:
  - *Accuracy* answers the question, “What percentage of calls to `contains` are
  correct?”
  - *Precision* answers the question, “What percentage of calls to `contains` returning
  true were correct?”
  - *Recall* answers the question, “Among all calls to `contains` on elements actually
  contained in the filter, what percent of them returned true?” (This one, as we
  know, will always be 100% for *Bloom filters*).

- example usages of RT(*Randomized Treaps*): keeping data read from a stream sorted, counting the
number of elements smaller (larger) than any given element of a dynamic set, and in
general all applications where we need to keep a dynamic set of elements in sorted
order, while supporting fast `search`, `insertion`, and `removal`.

- Treaps Usages:
```markdown
Treaps are useful in software that requires efficient dynamic ordered sets, range queries, and fast modifications while maintaining a balanced structure. Their probabilistic balancing makes them simpler than AVL or Red-Black Trees while still providing good performance. Below are some real-world applications:

1. Databases & Indexing

Use Case: Ordered Key-Value Storage
	•	Treaps can be used in in-memory indexes where ordered key-value access is needed.
	•	Unlike AVL and Red-Black trees, Treaps are easier to implement while maintaining expected O(log n) time for insertions, deletions, and lookups.

Example
	•	A column store database (like Apache Parquet) could use Treaps for efficient sorting and retrieval.
	•	Range queries (e.g., finding all keys in ￼) can be performed efficiently.

2. Competitive Programming & Algorithmic Problems

Use Case: Ordered Set with Fast Split/Merge
	•	Treaps support fast split and merge operations, unlike standard balanced trees.
	•	This makes them superior for problems involving dynamic ordered sets.

Example
	•	K-th smallest element in a dynamic array (using treap augmented with subtree sizes).
	•	Finding the number of elements ≤ X efficiently.

Implementation Trick:
To store elements dynamically in an ordered fashion while allowing fast order statistics, a Treap can be modified to store subtree sizes and efficiently compute the k-th smallest element in O(log n).

3. Version Control Systems (e.g., Git-like Systems)

Use Case: Managing File Changes Efficiently
	•	A Treap-based persistent data structure can store file versions.
	•	Split & merge operations allow efficient branching in O(log n).

Example
	•	Git-like distributed version control systems where commits and branches are handled as tree nodes.

4. Network Routing (Load Balancing)

Use Case: Fast Dynamic Priority-Based Routing
	•	Since Treaps are self-balancing and allow fast updates, they can be used for load balancing and dynamic network routing.

Example
	•	A dynamic load balancer where each server is assigned a priority, and requests are distributed accordingly.
	•	Treaps allow quick insertion and removal of servers while maintaining a priority-based search tree.

5. Text Editors & Text Processing

Use Case: Efficiently Handling Large Text Buffers
	•	Rope Data Structure: Treaps can be used to implement “ropes,” which are tree-based strings allowing fast insertion, deletion, and splitting.

Example
	•	Modern text editors (like Sublime Text, VS Code) use ropes for efficient undo/redo operations.
	•	Large text file processing, where inserting/deleting from the middle of a string needs to be O(log n).

6. AI & Game Development (Pathfinding)

Use Case: Optimized A* Search with Dynamic Priority Queues
	•	Priority queues in AI game engines can be implemented with Treaps.
	•	Unlike heaps, Treaps allow fast merges, making them useful for dynamic graph search algorithms.

Example
	•	Pathfinding in AI-controlled games using A Search* where Treaps help in efficiently updating priority queues.

7. Data Compression Algorithms

Use Case: Huffman Coding Optimization
	•	Treaps can be used instead of heaps in Huffman encoding to efficiently maintain the priority of symbols.

Example
	•	Treap-based Huffman Trees allow better handling of streaming compression where symbols are dynamically inserted and removed.

8. Cryptocurrency & Blockchain (Efficient Transactions)

Use Case: Balancing Unspent Transaction Outputs (UTXOs)
	•	Blockchain transactions involve searching, inserting, and deleting UTXOs efficiently.
	•	A Treap can be used for UTXO indexing, enabling faster transaction validation.

Example
	•	A Bitcoin client could store unspent outputs in a Treap to achieve logarithmic search and deletion.

9. Augmented Data Structures

Treaps can be augmented with:
	•	Subtree size → Find the ￼th smallest element efficiently.
	•	Sum of subtree elements → Range sum queries in O(log n).
	•	Min/Max in subtree → Fast range minimum queries.

Example
	•	Dynamic ranking systems (e.g., chess player rankings, sports leaderboards).
	•	Efficient interval merging, such as for scheduling or reservations.

Conclusion

Treaps are highly useful in scenarios requiring:
✅ Ordered sets with fast insertions & deletions
✅ Efficient range queries & order statistics
✅ Dynamic priority handling
✅ Probabilistic balancing with simpler implementation than AVL/Red-Black Trees
```

- The analysis of the comparative performance and height of BSTs and Randomized
Treaps suggests that, while the latter requires slightly more memory and can be slower
in the generic case, when we don’t have any guarantee on the uniform distribution of
keys or on the order of the operations, using BSTs carries a far greater risk of becom-
ing a bottleneck.

- 