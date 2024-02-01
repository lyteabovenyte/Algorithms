'''
    write a program which takes as input an arrau of digits encoding a nonnegative decimal
    integer D and updated the array to represent the integer D+1
    
    input --> [1, 2, 9]  output --> [1, 3, 0]
'''

def increment_precision(arr):
    #finding the number represented in the arr
    number = arr[0] * 10 + arr[1]
    
    i = 2
    while i < len(arr):
        number = number * 10 + arr[i]
        i += 1
        
    number += 1 #increment number by one
    
    result_arr = []
    while number > 0:
        digit = number % 10
        result_arr.append(digit)
        number = number // 10
        
    return list(reversed(result_arr))


print( increment_precision([9, 9, 9]) )



#another implementation 

def increment_precision2(arr):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        arr[i] = 0
        arr[i - 1] += 1
        
    if arr[0] == 10:
        #There is a carry-out
        arr[0] = 1
        arr.append(0)
    return arr


print( increment_precision2([1, 2, 9]) )
        
        