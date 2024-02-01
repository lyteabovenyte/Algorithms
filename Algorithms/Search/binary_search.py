def binary_search(arr, wanted):
    '''
        works on sorted arrays.
    '''
    
    low = 0
    high = len(arr)
    
    while( low <= high ):
        mid = ( low + high ) // 2
        guess = arr[mid]
        
        if guess < wanted :
            low = mid + 1
            
        elif guess > wanted :
            high = mid - 1
            
        else:
            return mid
    
    return None