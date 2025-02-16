from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        import heapq
        
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        max_heap = [] # to store the elements

        # we use greedy algorithm to find the maximum profit we can get.
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            # at this stage, if max_heap is empty, we can't process further.
            if not max_heap:
                break
            
            # we add to w one by one from max_heap, with highest profits
            # for k time total.
            w -= heapq.heappop(max_heap)

        return w
        