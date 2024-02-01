'''
[6, 3, 8, 4, 5] --> [3, 4, 5, 6, 8]

'''

def bead_sort(arr):
    if any(not isinstance(val, int) or val < 0 for val in arr):
        raise TypeError('array only can contain non negative integers.')
    
    for _ in range(len(arr)):
        for i, (left, right) in enumerate(zip(arr, arr[1:])):
            if left > right:
                arr[i] -= left - right
                arr[i + 1] += left - right
                
    return arr

    