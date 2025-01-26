'''
    https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
'''
from typing import List

def canJump(nums: List[int]) -> bool:
    gas = 0
    for n in nums:
        if gas < 0:
            return False
        elif gas < n:
            gas = n
        gas -= 1
    return True

print(canJump([3,2,1,0,4]))

def canJump2(nums: List[int]) -> bool:
    max_so_far, last_index = 0, len(nums) - 1
    i = 0
    while i <= max_so_far and max_so_far < last_index:
        max_so_far = max(max_so_far, nums[i] + i)
        i += 1
    return max_so_far >= last_index

print(canJump2([3,2,1,0,4]))