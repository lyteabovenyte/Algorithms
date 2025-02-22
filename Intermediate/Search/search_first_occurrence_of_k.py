"""
    Search a sorted array for the first occurrence of k.
"""
import bisect
def pythonic_first_occurrence(arr, k):
    return bisect.bisect_left(arr, k)

print(pythonic_first_occurrence([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285))

def binary_search(arr, k):
    left, right, result = 0, len(arr) - 1, -1

    while left <= right:
        mid = right - left // 2
        if arr[mid] == k:
            result = mid
            right = mid - 1 # try to find lower index which is equal to k
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    return result

print(binary_search([-14, -10, 2, 108, 108, 243, 285, 285, 285, 401], 285))