'''
    Assuming the keys take one of three values, reorder the array so that all objects with
    the same key appear together. The order of the subarrays is not important.

'''

def reorder_by_key(arr):
    # create a dictionary to store the index for each value in lst:
    d = {}
    
    for i in range(len(arr)):
        if arr[i] not in d:
            d[arr[i]] = []
            d[arr[i]].append(i)
        else:
            d[arr[i]].append(i)
    
    result_arr = []
    for key, values in d.items():
        for _ in values:
            result_arr.append(key)
            
    return result_arr


print( reorder_by_key([3, 4, 1, 2, 1, 4, 1, 3]) )


#another implementation
def reorder_by_key2(arr):
    
    i = 0
    while i < len(arr):
        j = i + 1
        k = i + 1
        while j < len(arr):
            if arr[i] == arr[j]:
                arr[k], arr[j] = arr[j], arr[k]
                k += 1
            j += 1
        i = k 
    
    return arr

print( reorder_by_key2([3, 1, 2, 3, 1, 3]) )