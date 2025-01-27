"""
    https://leetcode.com/problems/product-of-array-except-self
"""
from typing import List

def product_except_self(nums: List[int]) -> List[int]:

    product = 1
    zeroCount = 0
    n = len(nums)
    result = [0] * n

    # Step 1: Calculate product of all non-zero elements and count zeros
    for num in nums:
        if num == 0:
            zeroCount += 1
        else:
            product *= num

    # Step 2: Handle the cases based on zero count
    if zeroCount > 1:
        return result  # More than one zero, all elements will be zero
    if zeroCount == 1:
        for i in range(n):
            if nums[i] == 0:
                result[i] = product
    else:
        # If there are no zeros, divide the total product by each element
        for i in range(n):
            result[i] = product // nums[i]

    return result

print(product_except_self([-1,1,0,-3,3]))

def product_except_self2(nums: List[int]) -> List[int]:
    n = len(nums)
    ans = [1] * n
    pre = 1
    for i in range(n):
        ans[i] = pre
        pre *= nums[i]

    post = 1
    for j in range(n - 1, -1, -1):
        ans[j] *= post
        post *= nums[j]
    return ans

print(product_except_self2([-1, 1, 0, -3, 3]))