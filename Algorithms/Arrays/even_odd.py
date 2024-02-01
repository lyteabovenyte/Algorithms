'''
your input is an array of integers, and you have to reorder it's entries so that the even entries appear first.

NOTE: 
    no additional space. ( the additional space complexity should be O(1) )
    time complexity: O(n)
'''
#bad news!!: this implementations contains deleting the entries, which requires moving all entries to it's left. :D 

def even_odd(arr):
    i ,j = 0, 0
    while i < len(arr):
        if arr[j] % 2 != 0:
            poped = arr.pop(j) # deletion and insertion in arrays take O(n)
            arr.append(poped)
        else:
            j += 1
        i += 1
    return arr


# instead of deleting the entries , we consider overwriting it.

def even_odd2(arr):
    i , j = 0 , len(arr) - 1
    while i < j:
        if arr[i] % 2 == 0:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i] # instead of deletions and insertion we consider swapping.
            
            j -= 1
    return arr



print( even_odd([4, 3, 7, 4, 6, 1, 0]) ) # --> [4, 4, 6, 0, 3, 7, 1]
print( even_odd2([4, 3, 7, 4, 6, 1, 0]) ) # --> [4, 0, 6, 4, 1, 7, 3]