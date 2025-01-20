'''
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
'''
def insertion_sort(arr):
    size = len(arr)
    i = 1
    while i < size:
        j = i
        temp = arr[i]
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1] # swap
            j -= 1
        arr[j] = temp
        i += 1
    return arr

def InsertionSort(A):
    for i in range(1, len(A)):
        j = i - 1
        x = A[i]
        while (j > -1 and A[j] > x):
            A[j + 1] = A[j] # swap
            j -= 1
        A[j + 1] = x
    return A

print(InsertionSort([4, 2, 6, 3, 7]))