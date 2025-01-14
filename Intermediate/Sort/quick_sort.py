#First solution --> Pivot is the first element in the arr, it's close to O(n)
def quick_sort(arr):
    if len(arr) < 2:
        return arr     # --> base case
    else:
        pivot = arr[0]
        smaller_than_pivot = [i for i in arr[1:] if i <= pivot]
        bigger_than_pivot = [i for i in arr[1:] if i > pivot]
        
        return quick_sort(smaller_than_pivot) + [pivot] + quick_sort(bigger_than_pivot)   # --> Recursive case
    
    
print( quick_sort([5, 2, 8, 3, 7, 4, 22]) )


#Second solution --> Pivot is the middle element in the arr, it's close to O(logn)
def quick_sort2(arr):
    if len(arr) < 2:
        return arr  # --> Base Case
    
    mid = len(arr) // 2
    
    pivot = arr[mid]
    arr.pop(mid)
    
    smaller_than_pivot = [i for i in arr if i <= pivot]
    bigger_than_pivot = [i for i in arr if i > pivot]
    
    return quick_sort2(smaller_than_pivot) + [pivot] + quick_sort2(bigger_than_pivot)


print( quick_sort2([7, 2, 5, 3, 8, 8, 9]) )
    