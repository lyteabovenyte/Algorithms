'''
    Given two sorted arrays, A and B, merge them such a way that the result is sorted to.
    merge them into A which has enough space for len(A) + len(B) result of the algorithm.
'''
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
    

# progress from the back.
def merge_sorted_arrays(a, b):

    i, j, write_index = a.length() - 1, b.length() - 1, a.size - 1
    while i >= 0 and j >= 0:
        if a[i] >= b[j]:
            a[write_index] = a[i]
            write_index -= 1
            i -= 1
        else:
            a[write_index] = b[j]
            j -= 1
            write_index -= 1
    
    # check if every element is checked in b
    # if a is exhausted sooner.
    if j > 0:
        a[:j + 1] = b[:j + 1]

    return a


a = Array([2, 3, 7, 8, 9], 10)
b = Array([0, 1, 4, 5, 6], 5)

for i in range(merge_sorted_arrays(a, b).size):
    print(f'{i}: {a[i]}')






    