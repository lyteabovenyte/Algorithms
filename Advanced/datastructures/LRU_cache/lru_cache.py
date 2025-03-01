"""
    Implementation of LRU-Cache API.
    
    A cache stores a certain number of entries (the maxSize argument for the constructor, in the API), 
    always allows you to set new entries, and retains elements
    based on the concrete cache's implementation of the eviction policy
    When `set` is called, if an entry with the same key already exists on the cache,
    the new value will overwrite the old one.
"""

