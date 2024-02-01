def removeElement(nums, val):
        
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        k = len(nums)
        i = 0
        while(i < k):
            if nums[i] == val:
                nums.remove(nums[i])
                k -= 1
            else:
                i += 1
        
        return nums, k
    
    
print(removeElement([1, 2, 3, 2, 3, 2, 1], 2))

# or you can:

def remove_elemet2(arr, ele):
    
    index = 0
    k = len(arr)
    
    for i in range(k):
        if arr[i] != ele:
            arr[index] = arr[i]
            index += 1
    
    return arr, index 


print(remove_elemet2([1, 2, 3, 4, 2, 3, 4, 2], 2))