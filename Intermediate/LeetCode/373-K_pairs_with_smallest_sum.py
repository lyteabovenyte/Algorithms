from typing import List


# without heap --> may limit storage and time complexity.
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        import itertools

        candidates = list(itertools.product(nums1, nums2))

        indexed_candidates = [[ele[0] + ele[1], i] for i, ele in enumerate(candidates)]

        indexed_sorted = sorted(indexed_candidates)

        res = []
        i = 0
        for _ in range(k):
            res.append(candidates[indexed_sorted[i][1]])
            i += 1

        return res
    

# with heap
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        import heapq

        min_heap = []
        result = []

        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and min_heap: 
            sum, i, j = heapq.heappop(min_heap)
            result.append(nums1[i], nums2[j])

            if j + 1 < len(nums2):
                heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

            k -= 1

        return result