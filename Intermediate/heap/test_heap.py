# ---- itertools.groupby() ------
from itertools import groupby

a = [4, 5, 6, 3, 2, 1, 7, 8, 9]

class Monotonic:

    def __init__(self):
        self._last = float('-inf')

    def __call__(self, curr):
        res = curr < self._last
        self._last = curr
        return res
    
print(list(
    list(group)[::-1 if is_dec else 1]
    for is_dec, group in groupby(a, Monotonic())
))

print("------------")

def k_smallest_pairs(nums1, nums2, k):
    import heapq
    import itertools

    candidates = list(itertools.product(nums1, nums2))
    print(candidates)
    
    indexed_candidates = list(([ele[0] + ele[1], i] for i, ele in enumerate(candidates)))
    print(f'Indexed_candidates: {indexed_candidates}')

    min_heap = []

    i = 0
    for ele in indexed_candidates:
        heapq.heappush(min_heap, ele)
        
    res = []
    for _ in range(k):
        res.append(heapq.heappop(min_heap))

print(k_smallest_pairs([1, 1, 2], [1, 2, 3], 2))