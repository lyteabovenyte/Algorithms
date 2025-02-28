#### Notes on LRU_cache and caching in general.

###### content:
- Avoiding computing things twice
- Introducing caching as a solution
- Describing different types of caches
- Designing an efficient solution for LRU cache
- Discussing MFU and other choices for handling priority
- Discussing caching strategies
- Reasoning about **concurrency** and **synchronization**
- Describing how caches can be applied in a sentiment analyzer’s pipeline

----

By using *lists*, *queues*, *hash tables*, and so on as building blocks, we will be able to create an
advanced data structure that can be used to quickly access values and computed
results that were recently accessed. although one could argue that a cache is more
than just a data structure; it’s a sophisticated component with several moving parts.

- **GPU**: *Graphics Processing Units* were originally designed to speed up *image processing and buffering* for display
devices. With the turn of the century they became increasingly used as general (parallel) computation devices,
so much so that they actually are the election choice, instead of CPUs (Central Processing Unit), for algebraic-
intensive tasks such as machine learning.

- **Cursors** are control structures that allow traversing a set of rows in a DB table; as a simplification, they can be
thought of as pointers to the next row to read in a portion of the table, and they are used to subsequently process rows
(either reading data or modifying it) one by one, as opposed to a batch read/write where a group of
records is read/written at once.

- **Sharding** consists in breaking down data, users or transactions (or all of them) in groups, each of which is
assigned to a different machine/cluster/data-center. This balances the loads and allows us to use smaller,
cheaper servers and databases for each group, ultimately allowing applications to scale better and in a cheaper
way.

- **adapters**: In software engineering, an *adapter* is a design pattern that allows two incompatible *interfaces* to work together. In this case, each social media platform might have a different API structure, but you want to create a common interface to interact with all of them in a uniform way.
- Example of Why You Need Adapters:
    - Twitter API: Uses OAuth authentication and provides JSON responses in a specific format.
     - Facebook API: Uses Graph API and has different authentication and response structures.
     - LinkedIn API: Uses REST with a different query structure.
- Instead of writing custom logic for each API everywhere in your application, you create an *adapter* that translates requests/responses into a standard format.