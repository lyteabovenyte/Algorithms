'''
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.
Insertion sort works similarly as we sort cards in our hand in a card game

'''

def insertion_sort(arr):
    
    size = len(arr)
    i = 1
    while i < size:
        j = i
        temp = arr[i]
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
        i += 1
    return arr
