"""
    Given strings in streaming fashion, and our algorithm 
    should return the k-longest element at any moment.
"""
import itertools
import heapq

def top_k(k, stream):
    # Entries are compared by their length.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        # push next_string and pop the shortest string in min_heap
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    
    # heapq.nsmallest --> Equivalent to:  sorted(iterable, key=key)[:n]
    return [p[1] for p in heapq.nsmallest(k, min_heap)]