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

- cool stuff with binary and being variable length:
```python
m = "100110101"
n = m.zfill(15) # changin m to be 15 length size, filling the leading zeros.
# or
n2 = '{:015b}'.format(11) # changing an integer to be in a specific length.
```

- the ith entry in nth row, in pascal triangle is the P(n, r). in fact we can use the pascal triangle to compute P(n ,r)

- note the ~ operator which is the corresponding index in an array from the left.

- `result = [[1] * n for i in range(n)]` is correct. `n * [[1] * n]` is a trap.

#### chapter 6. String

- important concepts about strings which differentiate them from arrays: comparison, joining, splitting, searching for substrings, replacing one string by another, parsing

- advanced string processing algorithms often use hash tables and dynamic programming

- strings are immutable, so concatenating a string into another string implies creating new one and then changing the original one with the new one

- alternative to immutable strings --> e.g `list` in python

- updating a mutable strings from the front is slow, so consider approach to do so and **write the values from the back**

- 
```python
chr(ord('0') + some_int) # convert some_int to the corresponding string of that int
```

- [functools.reduce vs itertools.accumulate](https://realpython.com/python-reduce-function/)

- The idea behind Python’s `reduce()` is to take an existing function, apply it cumulatively to all the items in an iterable, and generate a single final value. In general, Python’s reduce() is handy for processing iterables without writing explicit for loops. Python’s reduce() also accepts a third and optional argument called `initializer` that provides a **seed** value to the computation or reduction.

- **CStyle arrays** -contiguous preallocated blocks of memory. how can we create on?
```python
import ctypes
array_type = ctypes.py_objects * 3 # define the size of the array.
array = array_type() # creating an array of size 3 which is NULL at first
# now we have an array of size 3 which is NULL.
```

- just a self implemented Array which has room for further insertions:
```python
import ctypes
from typing import List

class Array:
    def __init__(self, arr: List, size):
        array_data_type = ctypes.py_object * size
        self.size = size
        self.arr = arr
        self.memory = array_data_type()
        self.index = 0

        for i, ele in enumerate(self.arr):
            self.memory[i] = ele

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.arr) and self.index < self.size:
            return None
        elif self.index >= self.size:
            raise StopIteration
        value = self.arr[self.index]
        self.index += 1
        return value
    
    # indexing into array
    def __getitem__(self, idx):
        return self.memory[idx]
    
    # changing values by their index
    def __setitem__(self, idx, val):
        self.memory[idx] = val

    # size returns the size of the array   
    def size(self):
        return self.size
    
    # length returns the length of the populated chunks of array
    def length(self):
        return len(self.arr)
```

- it's good to have a grasp on `functools.reduce` source function:
```python
def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value
```
- `x.isalnum()` used to detect alphanumeric characters.

- difference between `find()` and `index()`:
```python
s = "some test string"
s.find('-1 if not found') # returns the index, but return -1 if not found
s.index('ValueError if not found') # returns the index, but raises ValueError if not found
```

- `__contains__` magic method.
```python
l = ["amir", "loves", "fasting"]
for ele in l:
    if ele.__contains__("fast"):
        print("fast is present")
```

- `itertools.product` can save us from nested loops:
```python
class product(builtins.object)
  product(*iterables, repeat=1)
```
- Cartesian product of input iterables.  Equivalent to nested for-loops.
For example, product(A, B) returns the same as:  ((x,y) for x in A for y in B).

```python 
'''
  The leftmost iterators are in the outermost for-loop, so the output tuples
  cycle in a manner similar to an odometer (with the rightmost element changing
  on every iteration).

  To compute the product of an iterable with itself, specify the number
  of repetitions with the optional repeat keyword argument. For example,
  product(A, repeat=4) means the same as product(A, A, A, A).

  product('ab', range(3)) --> ('a',0) ('a',1) ('a',2) ('b',0) ('b',1) ('b',2)
  product((0,1), (0,1), (0,1)) --> (0,0,0) (0,0,1) (0,1,0) (0,1,1) (1,0,0) ...

  Methods defined here:
  '''

  __getattribute__(self, name, /)
      Return getattr(self, name).
 
  __iter__(self, /)
      Implement iter(self).

  __next__(self, /)
      Implement next(self).

  __reduce__(self, /)
      Return state information for pickling.

  __setstate__(self, object, /)
      Set state information for unpickling.

  __sizeof__(self, /)
      Returns size in memory, in bytes
```