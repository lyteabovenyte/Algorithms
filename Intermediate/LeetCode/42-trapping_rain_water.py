"""
    https://leetcode.com/problems/trapping-rain-water
    level: Hard
"""
from typing import List
# may get Time Limit on large inputs
def trap(height: List[int]) -> int:
    pv = [0 for _ in range(len(height))]

    for i in range(1, len(height) - 1): 
        element = min(max(height[:i]), max(height[i + 1:])) - height[i]
        pv[i] = element if element > 0 else 0

    return sum(pv)

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))

# to defeat the Time Limit we compute the max_backward upfront.
def faster_tarp(self, height: List[int]) -> int:
    total_sum = 0
    max_ = height[0]
    max_backward = [0] * len(height)
    max_so_far = height[-1]
    for k in range(len(height) - 1, -1, -1):
        max_backward[k] = max_so_far
        if height[k] > max_so_far:
            max_so_far = height[k]

    for i in range(1, len(height) - 1): 
        element = min(max_, max_backward[i]) - height[i]
        if height[i] > max_:
            max_ = height[i]
        total_sum += element if element > 0 else 0

    return total_sum

