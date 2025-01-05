''' 
    Given a sorted array, delete the duplicates from it and return the valid entries
'''

def my_sol(arr):
    i, j, k = 1, 0, 0
    while i < len(arr):
        if arr[i] != arr[j]:
            arr[k] = arr[j]
            k, i, j= k + 1, i + 1, j + 1
        else:
            i, j = i + 1, j + 1
    arr[k] = arr[i - 1]
    arr[k + 1:] = [0] * (i - k - 1)

    # returning the number of valid entries
    num_valid = next(i for i, ele in enumerate(arr) if ele == 0)
    return arr, num_valid

def delete_dup(arr):
    if not arr:
        return 0
    
    write_index = 1
    for i in range(1, len(arr)):
        if arr[write_index - 1] != arr[i]:
            arr[write_index] = arr[i]
            write_index += 1
    arr[write_index:] = [0] * (len(arr) - write_index)
    # returing the number of distinct elements.
    return arr, write_index


print(my_sol([2, 3, 5, 5, 7, 11, 11, 11, 11]))
print(delete_dup([2, 3, 5, 5, 7, 11, 11, 11, 11]))