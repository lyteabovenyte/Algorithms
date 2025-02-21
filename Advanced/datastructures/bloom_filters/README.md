#### Bloom-filters: Reducing the memory for tracking content.

- A Bloom Filter is a **probabilistic data structure** that is highly space-efficient and is used for **set membership** testing. It helps determine whether an element is definitely not in a set or probably in the set but never gives false negatives (i.e., if it says an element is not in the set, it’s 100% correct). (Handles massive datasets with minimal memory overhead.)

- an associative array is composed of a collection of (key, value) pairs such that:
  - each possible key appears at most once.
  - each value can be retrieved directly through the corresponding key.

- looking through a list for a certain entity is a common problem that has a specific name for itself, *dictionary problem*
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

- Of course, compared to the O(1) amortized running time of hash tables, even bal
anced BSTs don’t seem like a good choice for implementing an associative array. The
catch is that while their performance on the core methods is slightly slower, BSTs allow
a substantial improvement for methods like finding the predecessor and successor o
key, and finding minimum and maximum: they all run in O(ln(n)) asymptotic time
for BSTs, while the same operations on a hash table all require O(n) time.
Moreover, BSTs can return all keys (or values) stored, sorted by key, in linear time,
while for hash tables you need to sort the set of keys after retrieving it, so it takes O(M +
n*ln(n)) comparisons.

- Bloom-fitlers:
    - Basic Bloom filters don’t store data; they just answer the question, is a *datum* in
	the set? In other words, they implement a *hash set’s API*, not a hash table’s API.
	- Bloom filters require less memory in comparison to hash tables; this is the main
	reason for their use.
	- While a negative answer is 100% accurate, there might be *false positives*. 
	- It is not possible to delete a value from a Bloom filter. (altough some variants are developed to handle element removal)

- basic **Bloom_filter** don't store data, they just answer the question is the datum in the set or not. (set!).

- for implementing a *bloom_filter* we need basic building blocks to help us determine the API of our data strucutre:
    - Some way to read and write bits at any location in our filter's *buffer*
    - A *mapping* between a key in input and the bits' indices in the buffer
    - A set of deterministically generated hash functions that will be used to transform keys into a list of indices.
---
#### some of the many application of Bloom_filters:
- I/O fetchers
- Crawlers and indexing visited ones (to prevent the loop, while crawling)
- Routers (storage within them)
- caching (hits and misses plus one-hit wonders)
- Cassandra uses Bloom filters for index scans to determine whether an SSTable has
data for a particular row.
Likewise, Apache HBase uses Bloom filters as an efficient mechanism to test
whether a StoreFile contains a specific row or row-col cell. This in turn boosts the
overall read speed, by filtering out unnecessary disk reads of HFile blocks that don’t
contain a particular row or row-column.
We are at the end of our excursus on practical ways to use Bloom filters. It’s worth
mentioning that other applications of Bloom filters include rate limiters, blacklists,
synchronization speedup, and estimating the size of joins in DBs
---
- bloom-filters are a tradeoff between accuracy and memory, the deterministic version of a bloom-filter is *hash-set*.

- any optimization problem can be expressed as a *decision problem* and vice versa.
- types of Randomized algorithms:
    - Las Vegas (Always correct, variable runtime):
        - These algorithms always produce the correct result, but their runtime varies depending on the randomness used.
    - Monte Carlo Algorithms (Fast, but May Be Incorrect):
        - These algorithms run in fixed time, but there is a small probability of returning an incorrect result.

- about vectorized algebra:
```markdown
Vector algebra is a branch of mathematics that deals with vectors, which are quantities having both magnitude and direction. It is widely used in computer science, physics, and engineering.

How does vector algebra relate to bloom-filters:
Modern CPUs support SIMD (Single Instruction, Multiple Data), which allows vectorized operations on multiple bits at once. Instead of processing one bit at a time, we can:
	1.	Store multiple elements in vector registers (e.g., AVX instructions in x86 CPUs).
	2.	Perform bitwise operations (AND, OR, XOR) on entire blocks of bits.
	3.	Compute multiple hash functions at once using vectorized instructions.

This allows parallel processing of Bloom filter bitmaps, leading to significant speed improvements.

so:
- Vector algebra helps optimize Bloom filters by enabling parallel operations on multiple bits
- Modern CPUs use SIMD and vectorized instructions to efficiently manipulate Bloom filter bit arrays.
```

---
#### LBF -> another variant of bloom-filter (layered bloom-filters) which is used for counting.
```markdown

Layered Bloom Filters (LBFs) are an extension of traditional Bloom Filters designed for approximate membership queries with counting capabilities. They maintain multiple layers of Bloom filters, each representing different frequency ranges, allowing approximate counting of elements in a set. Here’s how an LBF is used for counting:

1. Structure of Layered Bloom Filters

LBFs consist of multiple Bloom filters arranged in layers, where:
	•	Layer 0 is the base layer.
	•	Layer i stores elements whose estimated count falls in the range `2^i, 2^(i + 1) - 1`.
	•	Each layer has its own independent bit array.
	•	Each key is inserted into the lowest layer that can still approximate its count.

2. Counting a Key in an LBF

When inserting a key, it is placed in the lowest layer that can accommodate its estimated count.
	•	Insertion Process:
	•	Check the lowest layer first (Layer 0).
	•	If the element is already in that layer, move it to a higher layer when needed (i.e., when its count surpasses the current layer’s threshold).
	•	Each transition between layers approximately doubles the count estimate.
	•	Querying for Count:
	•	Check the highest layer where the key exists.

3. Example of Counting

Let’s assume we have an LBF with 3 layers:
	•	Layer 0 (stores counts between [1, 2]),
	•	Layer 1 (stores counts between [2, 3]),
	•	Layer 2 (stores counts between [4, 7]).

Scenario:
	1.	Insert key X → Added to Layer 0.
	2.	Insert X again → Detected in Layer 0, promoted to Layer 1.
	3.	Insert X again → Still in Layer 1 (count range [2,3]).
	4.	Insert X again → Moves to Layer 2 (count range [4,7]).

If we query X, we find it in Layer 2, so we estimate its count to be in the range [4, 7].

4. Advantages of LBF for Counting
	•	Memory efficiency: Uses less space than explicit counting Bloom filters (CBFs).
	•	Fast Approximate Counting: O(1) membership and count estimation.
	•	Lower False Positive Rate than CBF: Since frequent elements are moved to upper layers, LBFs reduce collision chances.

5. Use Cases of LBF
	•	Network security (DDoS detection): Detecting repeated IP addresses.
	•	Database systems: Keeping track of approximate query frequencies.
	•	Web caching: Identifying frequently accessed URLs.

```
- it's worth noting that both `insert()` and `contains()` in a LBF takes constant time and is independent of the number of elements which are added to the layered bloom filter.
- Randomized algorithms are divided into **Monte Carlo** and **Las Vegas** algorithms, depending on where the uncertainty lies.
- 