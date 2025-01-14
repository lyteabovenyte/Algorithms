'''
Bubble Sort is the simplest sorting algorithm that works 
by repeatedly swapping the adjacent elements if they are in the wrong order. 

Time Complexity:  O(n^2)
'''

def bubble_sort(arr):
    length = len(arr) - 1
    for i in range(length):
        swapped = False
        for j in range(length - i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr



def bubble_sort2(arr):
    i = len(arr) - 1
    while i > 0:
        j = 0
        while j < i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i -= 1
    return arr

