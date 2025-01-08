'''
    https://leetcode.com/problems/majority-element
'''
from collections import Counter

def majority_element_with_hashmap(nums):
    for key, value in dict(Counter(nums)).items():
        if value > len(nums) // 2:
            return key
        

def majority_element_without_hashmap(nums):
    res = majority = 0
    for n in nums:
        if majority == 0:
            res = n
        majority += 1 if res == n else -1
    
    return res


print(majority_element_without_hashmap([3, 2, 3]))

