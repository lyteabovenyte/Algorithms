'''
    Given an array, find the max length of a subarray whose elements are equal. 
'''

def max_length_subarray(arr):
    i, j = 0, 1
    max_length = 0
    while j < len(arr):
        if arr[i] == arr[j]:
            x = 1
            while arr[j] == arr[i]:
                i, j = i + 1, j + 1
                x += 1
                if j >= len(arr):
                    break
            max_length = max(x, max_length)
        else:
            i, j = i + 1, j + 1
    return max_length


print(max_length_subarray([2, 2, 3, 1, 1, 1, 1, 1, 5]))
            