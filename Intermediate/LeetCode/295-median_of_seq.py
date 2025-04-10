import heapq

def online_median(seq): 
    # min_heap stores the larger half seen so far
    min_heap = []
    # max_heap stores the smaller half seen so far
    # values in max_heap are negative
    max_heap = []
    result = []

    for x in seq:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))

        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) == len(max_heap) else min_heap[0])

    return result

print(online_median([1, 0, 3, 5, 2, 0, 1]))

# abstraction on top of our algorithm. from leetcode (295)
class MedianFinder:
    import heapq

    def __init__(self):
        self.max_heap = [] # smaller part
        self.min_heap = [] # larger part

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        if len(self.max_heap) > len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        return (0.5 * (self.min_heap[0] + -self.max_heap[0]) if len(self.min_heap) == len(self.max_heap) else self.min_heap[0])


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()