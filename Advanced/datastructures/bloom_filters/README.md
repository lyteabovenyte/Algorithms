#### Bloom-filters: Reducing the memory for tracking content.

- an associative array is composed of a collection of (key, value) pairs such that:
  - each possible key appears at most once.
  - each value can be retrieved directly through the corresponding key.

- looking through a list for a certain entity is a common problem that has a specific name for itself, *dictionary problem*
- why sorting has an average time complexity of O(n log n): gpt answers:
```markdown
In sorting algorithms, the best case time complexity depends on the algorithm used. The claim that the best case is ￼ applies to comparison-based sorting algorithms, such as Merge Sort, Quick Sort, and Heap Sort. However, it is important to clarify when and why this happens.

1. Lower Bound for Comparison-Based Sorting: ￼

Sorting must determine the correct order of elements, and in comparison-based sorting, we can think of the process as a decision tree where each internal node represents a comparison between two elements.

Decision Tree Model Explanation
	•	A comparison-based sorting algorithm works by comparing elements and making decisions based on the results.
	•	If we visualize this process as a binary decision tree, where each comparison splits the possible orderings into two branches, the tree has at most ￼ leaves (one for each possible permutation of ￼ elements).
	•	The height of a binary tree with ￼ leaves is at least:
￼
	•	Since sorting requires going from the root of the decision tree to a leaf, the minimum number of comparisons required in the worst case and average case is ￼.
	•	This means that no comparison-based sorting algorithm can be asymptotically faster than ￼ in the worst or average case.

Thus, in the best case, some algorithms can perform better than ￼ (e.g., QuickSort when already sorted), but in general, most divide-and-conquer sorts still take ￼ in the best case.

2. Sorting Algorithms with ￼ Best Case

Some sorting algorithms always run in ￼ time, even in the best case:
	•	Merge Sort: It always splits the array into two halves and merges them back, leading to a guaranteed ￼ complexity in the best, worst, and average cases.
	•	Heap Sort: Even in the best case, inserting elements into a heap and extracting them still results in ￼.

3. Sorting Algorithms with Better Best-Case Performance

Some algorithms can be better than ￼ in the best case:
	•	QuickSort (Best Case: ￼, Worst Case: ￼):
	•	If the pivot selection is always ideal (splitting the array into equal halves), it runs in ￼.
	•	However, if the array is already sorted and the pivot is always the smallest or largest element (bad choice), it degrades to ￼.
	•	With optimizations like randomized pivot selection, the worst case can be avoided.
	•	Insertion Sort (Best Case: ￼, Worst Case: ￼):
	•	If the array is already sorted, Insertion Sort just performs ￼ comparisons and no swaps.
	•	However, in the worst case (fully reversed array), it takes ￼ time.
	•	Timsort (Best Case: ￼, Worst Case: ￼):
	•	Used in Python’s sorted(), it is a hybrid sorting algorithm that runs in linear time for nearly sorted data.

4. Can We Do Better Than ￼?
	•	Yes, but only for special cases:
	•	If we do not use comparisons, we can achieve linear time sorting.
	•	Examples include Counting Sort, Radix Sort, and Bucket Sort, which run in ￼ under certain conditions (when elements are integers within a small range).

Conclusion
	•	For general-purpose comparison-based sorting, the best case can still be ￼ (e.g., Merge Sort, Heap Sort).
	•	Some algorithms (like Insertion Sort, Timsort) perform better in special cases (e.g., nearly sorted data).
	•	Sorting can be done in ￼ time with non-comparison-based methods (Counting Sort, Radix Sort).
```

- The main take away for hash
tables is that they are used to implement associative arrays where the possible values to
store come from a very large set (for instance, all possible strings or all integers), but
normally we only need to store a limited number of them. If that’s the case, then we
use a hashing function to map the set of possible values (the *domain*, or source set) to
a smaller set of M elements (the *codomain*, or target set), the indices of a plain array
where we store the values associated to each key.

- Hash tables, use a few strategies to resolve conflicts, such as *chaining* or *open addressing*.

- we distinguish hash maps and
hash sets. The former allows us to associate a value to a key; the latter only to record the
presence or absence of a key in a set. Hash sets implement a special case of dictionary,
the *Set*. With respect to our definition of dictionary as an abstract data structure, a set is a specialization of a dictionary, where the value type is set to *Boolean*; the second parameter to insert becomes redundant, as the
*value* associated with a key in the hash set will be implicitly assumed to be `true`.

- all operations in a hash table (and hash set) can be performed in amortized O(1) time.

- Of course, compared to the O(1) amortized running time of hash tables, even bal-
anced BSTs don’t seem like a good choice for implementing an associative array. The
catch is that while their performance on the core methods is slightly slower, BSTs allow
a substantial improvement for methods like finding the predecessor and successor o
key, and finding minimum and maximum: they all run in O(ln(n)) asymptotic time
for BSTs, while the same operations on a hash table all require O(n) time.
Moreover, BSTs can return all keys (or values) stored, sorted by key, in linear time,
while for hash tables you need to sort the set of keys after retrieving it, so it takes O(M +
n*ln(n)) comparisons.

- 