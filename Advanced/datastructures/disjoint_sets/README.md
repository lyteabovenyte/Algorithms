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