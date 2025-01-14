'''
    https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, j, k = 0, 0, 1
        while k < len(nums):
            if nums[i] == nums[k]: 
                i, k = i + 1, k + 1
            else:
                nums[j] = nums[i]
                i, k, j = i + 1, k + 1, j + 1
            if k == len(nums):
                nums[j] = nums[k - 1]
                break
        return j + 1