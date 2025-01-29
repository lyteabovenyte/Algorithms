"""
    https://leetcode.com/problems/3sum/description
    nums = [-1,0,1,2,-1,-4] --> output: [[-1,-1,2],[-1,0,1]]
"""
from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    # sort to simplify dup handling
    nums.sort()
    # using set to ensure uniqueness
    res = set()

    for i in range(len(nums) - 2):
        # handle dup
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # using set to ensure uniqueness
        seen = set()
        for j in range(i + 1, len(nums)):
            complement = -nums[i]-nums[j]
            if complement in seen:
                res.add((nums[i], complement, nums[j]))
            seen.add(nums[j])

    return list(map(list, res))

print(three_sum([-1,0,1,2,-1,-4]))
