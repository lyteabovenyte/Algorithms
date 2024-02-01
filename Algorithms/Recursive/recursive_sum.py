def recursive_sum(arr):
    
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])
    
print( recursive_sum([4, 3, 1, 2]) ) # --> outputs 10

