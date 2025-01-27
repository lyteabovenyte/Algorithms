"""
    https://leetcode.com/problems/jump-game-ii/
"""
from typing import List

# using greedy approach to get the minimum jumps to the end.
def jump_game_ii(nums: List[int]) -> int:
    jump, current_end, farthest = 0, 0, 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, nums[i] + i)
        if i == current_end:
            jump += 1
            current_end = farthest
    return jump

print(jump_game_ii([2, 3, 1, 1, 4]))