from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        max_heap = []
        for ele in nums:
            heapq.heappush(max_heap, -ele)

        for _ in range(k):
            result = heapq.heappop(max_heap)

        return result
