def merge(arr1, arr2):
    output_arr = []
    
    i = 0
    j = 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            output_arr.append(arr1[i])
            i += 1
        else:
            output_arr.append(arr2[j])
            j += 1
            
    
    while i < len(arr1):
        output_arr.append(arr1[i])
        i += 1
        
    while j < len(arr2):
        output_arr.append(arr2[j])
        j += 1
        
    return output_arr



print( merge([2, 4, 6, 8], [1, 3, 5, 7]) )