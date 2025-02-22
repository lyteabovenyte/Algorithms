#### Notes on Disjoint sets: Sub-Linear time processing. (Wolf in sheep's clothing)

- The disjoint Set data structure is generally used for dynamic graphs.
- We will use a **disjoint set** every time that we would like to account for the partitioning of an initial set of objects into disjoint groups (that is, subsets without any element
in common between them)
-  In a real *non-personalized recommender system*, we would track associations between products, measuring the *strength*
of the link as the confidence that when X is bought, Y is also. For that, we may compute
the number of purchases where both appear, divided by the total number of purchases
where at least Y appears. That would give us better insight about what goes with what,
we could define a threshold on the confidence for merging groups, and instead of picking a random item in the same group, show the top five strongest associations. (graph ???)
- the core API of Disjoint-sets are `find_partition()`, `are_disjoint()` and `merge()`.
- the concrete implementation uses a hash map internally to keep track of the association of each element with it's respective set.
- normally we are interested in the element that `are_disjoint()` and then merge the two partition.
- The data structure maintains a collection of non-overlapping (disjoint) sets, each of which is represented by some member of that set. They can be used in a wide variety of contexts but are particularly popular with graph problems such as finding the minimum spanning tree or strongly connected components.
- in a tree-like representation of a disjoint_sets, Each partition is uniquley identified by the root of the tree associated with the partition.
- **heuristics to improve the running time of Tree-like-disjoint-sets**:
    - we can easily keep track of the rank (aka size) of each tree,
      using linear extra space and performing constant-time extra operations in method
      `merge`, where we will update rank only for trees' roots. When we merge two trees, we will make sure to set as child the tree with the smallest number of nodes
    - the huristic here is called **path compression**. for each node in the trees, instead of storing a link to its parent, we can store one to the root of the tree. After all, we don’t
    really need to keep track of the history of the merges we performed; we just need to
    know at the current time what the root is for an element's partition—and find that out
    as quickly as we can.
- for the difference between tree-like and path-compression approach on disjoint_sets:
    - when using the path compression heuristic, we don’t update the root of all elements on `merge`, but we do update it on `find_partition`. So, the main difference from the older version is that we save the result of the recursive calls to `find_partition`, and we use it to update the current
    element’s root. Everything else remains exactly the same

---
#### Applications of disjoint_sets:
###### Graphs: Connected components
- For* undirected graphs*, there is a simple algorithm that uses disjoint sets to keep track of
their connected components, that is, areas of the graph that are interconnected. While connected components are usually computed using Depth First Search(DFS), we can use a disjoint set to keep track of the components while we scan all the graph’s edges.
###### MST: Kruskal’s Algorithm for Minimum Spanning Tree
- Kruskal's algorithm build a MST (minimum spanning tree) by:
  - sorting all the edges by weight
  - Using Disjoint Sets to check if adding an edge would form a cycle:
      - If the edge connects two different components, add it to the MST.
      - If the edge forms a cycle, ignore it.
  - Stopping when we have exactly N-1 edges (where N is the number of vertices).
- or
  - Starting with each vertex in a difference set.
  - Keeping a disjoint set of the graph vertices.
  - Going through the graph’s edges in order of increasing weight.
  - For each edge, if its extremes are not in the same partition, merge their components.
  - If all vertices belong to the same component, stop.

###### Clustering: finding a structure in raw data
- **Agglomerative hierarchical clustering** starts with each point in its own cluster (*partition*)
and continuously *merges* two points (and their clusters) until all clusters are merged
into one. The algorithm keeps a history
of this process, and it is possible to get a *snapshot* of the clusters created at any of the
steps. The exact point where this snapshot is taken is controlled by a few parameters
and determines the result of the algorithm.
