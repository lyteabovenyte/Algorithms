'''
    Given a sorted array and an integer m, update the array in a way
    that if a element appear more than m times, it appears exactly min(2, m)
    times.
'''

def min_2_and_m(arr, m):
    i, j, k = 0, 1, 0
    while j < len(arr):
        if arr[j] != arr[i]:
            arr[k] = arr[i]
            i, j, k = i + 1, j + 1, k + 1
        if arr[j] == arr[i] and j < len(arr):
            x = 1
            while arr[j] == arr[i] and j < len(arr):
                i, j = i + 1, j + 1
                x += 1
            w = min(m, 2)
            while w > 0:
                arr[k] = arr[i]
                k += 1
                w -= 1
            # i, j = i + 1, j + 1
    arr.append(arr[j])
    arr[k:] = [0] * (len(arr) - k)
    return arr


print(min_2_and_m([2, 3, 5, 5, 5, 5, 7, 11, 11, 11, 11], 2))

