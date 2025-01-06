'''
    Given an array, rearrange it to have A[1] <= A[2] >= A[3] <= A[4] ...
'''

def my_sol(arr):
    i = 0
    while i < len(arr):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1
        if i >= len(arr) - 1:
            break
        if arr[i] < arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1
        if i >= len(arr) - 1:
            break
    return arr

# elegant way of eating pizza
def alternative_array(arr):
    for i in range(len(arr)):
        arr[i: i + 2] = sorted(arr[i: i + 2], reverse=i % 2)
    return arr


print(my_sol([3, 1, 2, 8, 5, 7, 6]))
print(alternative_array([3, 1, 2, 8, 5, 7, 6]))