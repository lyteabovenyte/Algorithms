### element of programming

##### intro:
- [know how to impelment a list with dynamic allocation](https://essinstitute.in/exploring-dynamic-and-static-memory-allocation-in-python/)

- **helpful pdf** [cs.cum.edu lectures](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15850-f20/www/notes/)
(Note: you can change the last part of the url to go to a specific lecture e.g lec11.pdf --> streaming algorithms)

- Apply patterns: **patterns**-general reusable solutions to commonly occurring problems-can
be a good way to approach a baffling problem. Examples include **finding a good data structure**,
seeing if your problem is a good fit for a general algorithmic technique, e.g., **divide-and-conquer**,
**recursion**, or **dynamic programming**, and **mapping** the problem to a **graph**.

- [Python collections](https://docs.python.org/3/library/collections.html) or in [intermediate python](https://book.pythontips.com/en/latest/collections.html)

#### chapter 1. Primitive Types

- The usage of `^` comes to the **parity**. `XOR` in python.
- The usage of **caching** in comutative and associative operations
- **remember the tricks of `x & (x - 1)` vs `x & ~(x - 1)`**
- trick for sorting a list of namedtuple based on a specific key:
```python
from operator import attrgetter
import collections

Point = collections.namedtuple('Point', ('x', 'y'))
lst = [P1, P2, P3, P4]
# sorting based on y
sorted_lst = sorted(lst, key=attrgetter('y'))
```

#### chapter 5. Arrays
###### books bootcamp on array notes:
  - when working with arrays, we should take advantage of the fact that we can operate efficiently on both ends. (for **two-pointers** solutions)

  - Array problems often have simple brute-force solutions that use O(n) *space*, but there are subtler solutions that use the array itself to reduce *space* complexity to O(1).

  - Filling an array from the front is slow, so see if it's possible to **write values from the back**

  - Instead of deleting an entry (which requires moving all entries to its left), consider **overwriting** it.

  - When dealing with integers encoded by an array consider processing the digits from the *back* of the array. Altemately, **reverse the array so the least-significant digit is the first entry**.

  - Be comfortable with writing code that operates on **subarrays**

  - Don't worry about preserving the integrity of the array (sortedness, keeping equal entries together, etc.) **until it is time to return**.

  - an array can serve as a good data structure when you know the distribution of the elements in advance. For example, a Boolean array of length W is a good choice for representing a subset
  of {0, 1, ... ,W - 1}. (When using a Boolean array to represent a subset of {1, 2, ..., n} allocate anarray of size n+1 to simplify indexing.)
  
  - when operating on 2D arrays, use **parallel logic** for rows and for columns

- The difference between **shallow** and **deep** copying is only relevant for compound objects (objects that contain other objects, like lists or class instances):
  - A shallow copy constructs a new compound object and then (to the extent possible) inserts *references* into it to the objects found in the original.
  - A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

- Key methods for list include min(A), max(A), binary search for sorted lists
(bisect.bisect(A,6), bisect.bisect_left(A,6), and bisect.bisect_right(A,6)),
A.reverseO (in-place), reversed(A) (retums an iterator), A.sort()(in-place), sorted(A)
(returns a copy), del A[i] (deletes the i-th element), and del A[i: j] (removes the slice).

- [bisect] module: This module provides support for maintaining a list in *sorted* order without having to sort the list after each *insertion*. For long lists of items with expensive comparison operations, this can be an improvement over linear searches or frequent resorting. The module is called bisect because it uses a basic bisection algorithm to do its work. Unlike other bisection tools that search for a specific value, the functions in this module are designed to **locate an insertion point**.

- cool thing that can be done using slicing:
```python
l = [1, 2, 3, 4, 5, 6]
l[:-1] # removes the last element
l[k:] + l[:k] # rotate l by k to the left
l[::-1] # reverse
l2 = l[:] # shallow copy
```

- **partitioning strategy** based on a sepecific pivot.

- getting the count of every distinct value in the list:
```python
from collections import Counter
l = # some list
c_m = Counter(l)
```

- 