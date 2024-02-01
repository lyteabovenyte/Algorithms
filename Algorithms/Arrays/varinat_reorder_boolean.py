'''
    Given an array A of n object with Boolean-valued keys, reordre the array 
    that have he key False appear first.
'''

def reorder_boolean(arr):
    i, k = 0, 0
    
    while i < len(arr):
        if arr[i] == False:
            arr[i], arr[k] = arr[k], arr[i]
            k += 1
        i += 1
    return arr


print( reorder_boolean([True, False, False, True, False]) )