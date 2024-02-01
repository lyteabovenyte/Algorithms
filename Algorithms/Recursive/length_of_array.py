'''
    recursive way of counting the length of an array.

'''

def count_length_of_arr(arr):
    
    if len(arr) == 0:
        return 0
    else:
        return 1 + count_length_of_arr(arr[1:])
        
        
print( count_length_of_arr([3, 2, 5, 6, 7, 8]) )
    