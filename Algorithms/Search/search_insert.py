"""
Helper methods for implementing insertion sort.

Given a sorted array and a target value, return the index if the target is
found. If not, return the index where it would be if it were inserted in order.

    For example:
    [1,3,5,6], 5 -> 2
    [1,3,5,6], 2 -> 1
    [1,3,5,6], 7 -> 4
    [1,3,5,6], 0 -> 0
    
WARNING: following algo is True if and only if , the array is sorted.

"""
# First solution with O(n) Time complexity, Linear
def search_insert_linear(arr, val):
    if val in arr:
        return arr.index(val)
    else:
        k = 0
        for i in range(len(arr)):
            if arr[i] < val:
                k += 1
    
    return k

# Second solution with O(logn) Complexity, log
def search_insert_log(arr, val):
    low = 0
    high = len(arr) - 1
    mid = high // 2
    
    while high >= low:
        if val > arr[mid]:
            mid += 1
            low = mid
        else:
            mid -= 1
            high = mid
    
    return low

