'''
    write a program that takes an array A and an index i into A,
    and rearranges the elements such that all elements less than A[i] ( the "PIVOT" )
    appear first, followed by elements equal to the pivot, followed by elements greater than the pivot 

'''

# solution with list comprehension --> bad space complexity
def dutch_national_flag(arr, i):
    smaller_than_pivot = [ch for ch in arr if ch < arr[i]]
    equal_to_pivot = [ch for ch in arr if ch == arr[i]]
    greater_than_pivot = [ch for ch in arr if ch > arr[i]]
    
    return smaller_than_pivot + equal_to_pivot + greater_than_pivot





def dutch_national_flag2(arr, x):
    '''
        we can avoid using O(n) additional space at the cost of increase time complexity as follows
        space complexity = O(1)
        time complexity = O(n^2)
    '''    
    pivot = arr[x]
    
    for i in range(len(arr)):
        # First pass: group elements smaller than pivot
        for j in range(i + 1, len(arr)):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
        
    # Second pass: group elements larger than pivot
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than pivot, cause
        # first pass has moved them to the start off the arr
        for j in reversed(range(i)):
            if arr[j] > pivot:
                arr[i], arr[j] = arr[j], arr[i]
                break
            
    return arr


# even better implementation

def dutch_national_flag3(arr, x):
    '''
        time complexity = O(n)
        space complexity = O(1)
    '''
    
    pivot = arr[x]
    # group elements smaller than pivot
    smaller = 0
    for i in range(len(arr)):
        if arr[i] < pivot:
            arr[i], arr[smaller] = arr[smaller], arr[i]
            smaller += 1
        
    # group elements larger than pivot
    larger = len(arr) - 1
    for i in reversed(range(len(arr))):
        if arr[i] < pivot:
            break
        elif arr[i] > pivot:
            arr[i], arr[larger] = arr[larger], arr[i]
            larger -= 1
    return arr



print( dutch_national_flag3([4, 6, 8, 2, 7, 3, 5], 1) )
print( dutch_national_flag2([3, 6, 1, 8, 5, 6, 9, 3], 1) )
print( dutch_national_flag([4, 6, 8, 2, 7, 3, 5], 1) )