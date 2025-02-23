#### Tries, radix trie: Efficient string search.

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

- aaec7b