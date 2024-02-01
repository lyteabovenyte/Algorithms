'''
    problem at: https://leetcode.com/problems/contains-duplicate/submissions/
'''


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
    
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        for value in d.values():
            if value >= 2:
                return True

        return False