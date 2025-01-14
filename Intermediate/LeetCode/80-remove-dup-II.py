'''
    https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
'''

def remove_dups_II(nums):
    i, k = 2, 2
    while i < len(nums):
        if nums[i] == nums[k-2]:
            i += 1
        else:
            nums[k] = nums[i]
            i += 1
            k += 1
    nums[:] = nums[:k]
    return nums



print(remove_dups_II([0, 0, 0, 1, 1, 1, 1, 2, 3]))