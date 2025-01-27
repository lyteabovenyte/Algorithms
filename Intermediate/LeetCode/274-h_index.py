"""
    https://leetcode.com/problems/h-index/
"""
from typing import List

def h_index(citation: List[int]) -> int:
    citation.sort()
    n = len(citation)
    # the cool thing about sorted citaiton is that
    # if the element at index i is greater than len(citations) - i
    # then we are sure that all the element to the right are greater also
    for i, ele in enumerate(citation):
        if n - i <= ele:
            return n - i
    return 0

print(h_index([1,3,1]))