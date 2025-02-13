"""
    Given as input a set of sorted list and the algorithm should return the union in the sorted fashio
    in a single output list.
"""
import heapq

def merge_sorted_files(sorted_arrays):
    min_heap = []

    # Builds a list of iterators for each array in sorted_arrays
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterators in min_heap
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            # we keep track of i -> to determine which iter we extract from
            heapq.heappush(min_heap, (first_element, i)) 

    result = []
    while min_heap:
        smallest_entry, smallest_entry_i = heapq.heappop(min_heap)
        smallest_entry_iter = sorted_arrays_iters[smallest_entry_i]
        result.append(smallest_entry)
        next_element = next(smallest_entry_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_entry_i))
    return result


# pythonic -> heapq.merge() -> takes multiple input and merges them.
# Similar to sorted(itertools.chain(*iterables)) 
def merge_sorted_arrays(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))
