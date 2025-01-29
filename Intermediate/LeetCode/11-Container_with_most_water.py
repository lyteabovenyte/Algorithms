"""
    https://leetcode.com/problems/container-with-most-water
"""
from typing import List

def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1

    max_so_far = 0
    while left < right:
        max_so_far = max(max_so_far, (min(height[left], height[right]) * (right - left)))

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_so_far

print(max_area([4, 1, 6, 2, 5]))
