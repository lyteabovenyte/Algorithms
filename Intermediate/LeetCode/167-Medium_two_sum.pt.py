"""
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
"""
from typing import List

def two_sum_medium(numbers: List[int], target: int):


    for i, ele in enumerate(numbers):
        tg = target - ele
        try:
            if i + 1 >= len(numbers):
                return False
            idx = numbers[i+1:].index(tg)
            return [i + 1, idx + i + 2]
        except ValueError:
            continue

# benefits from the fact that the numbers array is in non-decreasing order
def faster_two_sum_medium(numbers: List[int], target: int):
    left, right = 0, len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]

        if total == target:
            return [left + 1, right + 1]
        elif total > target:
            right -= 1
        else:
            left -= 1

    # no need to return anything cause the problem assured that there is at least one sol.

print(faster_two_sum_medium([2, 9, 4, 8, 6], 8))