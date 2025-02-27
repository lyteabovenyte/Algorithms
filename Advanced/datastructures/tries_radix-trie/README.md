#### Tries, radix trie: Efficient string search.


---
#### Tries:

- find all the keys in the container that starts with the same prefix.
- contract with the client within the API of this data structure(string_container or prefix_tree):
  - Besides all the operations of a regular, plain container(`insert`, `remove`, `contain`), this structure allows us to search for the longest prefix of a string that is stored in it and return all the stored strings that start with a certain prefix.

- **Tries** were originally developed as a compact, efficient way to search strings in files;
the idea behind this data structure is providing a way to reduce redundancy by storing common prefixes of strings just once.

- in a Trie, the fact that all words are stored in the edges, shows that all the descendants of a node shares a common prefix: the path from root to their common parent.(Lowest-common-ancestor[../../Intermediate/Binary_Trees/LCA.py](LCA algorithm))

- While for spell checkers storing a Boolean in each node could be enough (after
all, we only need to know whether a word is in a dictionary), tries are often used to
store or index words in texts. If that’s the case, we often need to know either how
many *occurrences* of a word appear in the text or the positions where they appear. In
the former situation we can store a *counter* in each node and only key nodes will have
a positive value. In the latter we will instead use a *list of positions*, storing the index in
the text where each occurrence starts.

- **think about indexing words in Trie!!**

- let’s also recap the pros and cons of using tries, and when we should prefer a trie over a BST:
  - pros:
    - The search time only depends on the length of the searched string.
    - Search misses only involve examining a few characters (in particular, just the
    longest common prefix between the search string and the corpus stored in the
    tree).
    - There are no collisions of unique keys in a trie.
    - There is no need to provide a hash function or to change hash functions as
    more keys are added to a trie
    - A trie can provide an alphabetical ordering of the entries by key.
  - cons:
    - Tries can be slower than hash tables at looking up data whenever a container is
    too big to fit in memory. Hash tables would need fewer disk accesses, even down
    to a single access, while a trie would require O(m) disk reads for a string of
    length m.
    - Hash tables are usually allocated in a single big and contiguous chunk of memory, 
    while trie nodes can span the whole heap. So, the former would better
    exploit the principle of locality.
    - Tries have memory overhead for nodes and references. As we have seen, some
    implementations require each node to store an array of k edges, where k is
    the alphabet used —even if the node has few or no children at all.

---
###### In summary, the advice could be to use tries when you have to frequently perform preix searches (*longestPrefix* or *keysWithPrefix*). Use hash tables when data is stored on slow supports like disk or whenever *memory locality* is important. In all intermediate cases, profiling can help you make the best decision.

---

- We have seen that we can use associative arrays, dictionaries in particular, to implement nodes, only storing edges that are not null. Of course, this solution comes at a cost: not only the cost to access each edge (that can be the cost of hashing the character plus the cost of resolving key conflicts), but also the cost of resizing the dictionary
when new edges are added.

----
#### Radix Tries:

- If, however, an intermediate node stores no key and only has one child, then it carries no relevant information; it's only a forced step in the path.
*Radix tries* (aka radix trees, aka Patricia trees) are based on the idea that we can
somehow *compress* the path that leads to this kind of nodes, that are called *pass-through* nodes.

- As one of the main uses for tries is to implement
text-based dictionaries, the touchstone will often be *hash tables*.

- implementing spell-check with Tries: (**How would we suggest the correct version of a typo?**)
    - Let's say that the word *w* we are checking has *m* characters, and we can accept suggestions differing by at most *k* characters from *w*: in other words, we want words whose
    *Levenshtein distance* (also known as edit distance) is at most *k*.
    - For each node N, we check the array holding the edit distances:
        - If all distances in the array are greater than out maximum tolerance, then we
        can stop; there's no need to traverse its subtree any further (because the dis-
        tances can only grow).
        - Otherwise, we keep track of the last edit distance (the one for the whole search
        string), and if it's the best we have found so far, we pair it with current node's
        key and store it.
- **Burstsort** is a *cache-efficient* sort algorithm that works similarly to *MSD* (Most Signifi-
cant Digit) radix sort. However, burstsort is cache-efficient and even faster than radix sort!
They both have the same asymptotic running time, O(n * M), which is a theoretical
lower bound for sorting n strings of length M, but burstsort creates results twice as fast
by exploiting *locality of reference and better memory distribution*.

- String prefixes are a key factor for this new data structure, which in turn allows
us to efficiently perform queries to find strings with a common prefix or, vice
versa, given a string find its longest prefix in the dataset.

- From spell-checkers to bioinformatics, many applications and fields manipulat-
ing strings can benefit from using tries.