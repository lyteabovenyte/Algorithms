"""
    An array is said to be k-increasing-decreasing which, 
    it increases up to a certain index, then decrease then increase for a total number of k times.
    Design an efficient algorithm for sorting a k-increasing-decreasing array.

    Approash: Cast this in terms of combining k sorted arrays.
"""
import heapq
import itertools

from merge_sorted_files import merge_sorted_files

def sort_k_increasing_decreasing(array):
    # Decompose array into a set of sorted arrays
    sorted_subarray = []
    INC, DEC = range(2)
    subarray_type = INC
    start_index = 0
    for i in range(1, len(array) + 1):
        if (i == len(array) or # array ended, adds the last element.
            (array[i - 1] > array[i] and subarray_type == INC) or
            (array[i - 1] < array[i] and subarray_type == DEC)):
            sorted_subarray.append(array[start_index:i] if subarray_type == INC
                                   else array[i - 1: start_index - 1: - 1])
            
            start_index = i
            subarray_type = (DEC if subarray_type == INC else INC)
    
    return list(heapq.merge(*sorted_subarray))
        
print(sort_k_increasing_decreasing([4, 5, 6, 3, 2, 1, 7, 8, 9]))


# pythonic sol
def sort_k_increasing_decreasing_pythonic(A):
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')

        def __call__(self, curr):
            res = curr < self._last
            self._last = curr
            return res

    return merge_sorted_files([
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A, Monotonic())
    ])